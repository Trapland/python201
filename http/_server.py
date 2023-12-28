import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import importlib
import appconfig
import inspect
import routes
import time
import json
import random
import dao

class MainHandler(BaseHTTPRequestHandler):
    sessions = {}
    
    def __init__(self, request, client_address, server) -> None:
        self.response_headers = dict()
        super().__init__(request, client_address, server)
    
    def do_GET(self) -> None:
        # Робота з сесією
        cookies_header = self.headers.get('Cookie', '')
        cookies = dict( cookie.split('=') for cookie in
            cookies_header.split('; ') if '=' in cookie )
        print( cookies )
        # self.send_header( 'Set-Cookie', 'session-id=123' )
        if 'session-id' in cookies and cookies['session-id'] in MainHandler.sessions :  # Є сесія для даного запиту
            # вилучаємо дані зі статичного сховища і переносимо у self
            self.session = MainHandler.sessions[ cookies['session-id'] ]
        else :   # Немає сесії для запиту
            # стартуємо сесію - генеруємо id, якого немає у sessions
            while True :
                session_id = str( random.randint(1000, 9999) )
                if not session_id in MainHandler.sessions :
                    break
            # встановлюємо заголовок Cookie
            self.response_headers['Set-Cookie'] = f'session-id={session_id}'
            # утворюємо "сховище" для даних
            MainHandler.sessions[session_id] = {
                'id': session_id,
                'timestamp': time.time()
            }
            self.session = MainHandler.sessions[ session_id ]
        print( self.session )
        # кінець з сесіями - тепер у handler є self.session
        parts = self.path.split('?')
        path = parts[0]
        query_string = parts[1] if len(parts) > 1 else None
        
        # перевіряємо чи запит - це файл
        if '../' in path or '..\\' in path:
            self.send_404()
            return
        filename = appconfig.WWWROOT_PATH  + path
        # print(self.path, filename,os.path.isfile(filename))
        if os.path.isfile(filename):
            self.flush_file(filename)
            return
        # розбираємо запит за принципом /controller/action
        path = routes.predefined_urls.get(path, path)
        
        path_info = routes.parse_path(path)

        controller_module   = importlib.import_module(path_info['controller'])
        controller_class    = getattr(controller_module,path_info['controller'])
        controller_instance = controller_class(self)
        controller_action   = getattr(controller_instance,path_info['action'])

        if controller_action:
            controller_action()
        else:
            self.send_404()
            return
        

    
    def flush_file(self, filename):
        if not os.path.isfile(filename):
            self.send_404()
            return
        ext = filename.split(".")[-1]
        if ext in ("css", "html"):
            content_type = "text/" + ext
        elif ext == "js":
            content_type = "text/javascript"
        elif ext in ("jpg", "jpeg"):
            content_type = "image/jpeg"
        elif ext in ("png", "bmp"):
            content_type = "image/" + ext
        elif ext in ("py", "ini", "env", "jss", "php"):
            self.send_404()
            return
        else:
            content_type = "application/octet-stream"
        
        self.send_response(200, 'OK')
        self.send_header('Content-Type', content_type)
        self.end_headers()
        with open (filename, mode="rb") as f:
            self.wfile.write(f.read())
    
    def send_404(self) -> None:
        self.send_response(404, 'Not Found')
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write("<h1>Resource for request not found</h1>".encode())
    
    def log_request(self, code: int | str = "-", size: int | str = "-") -> None:
        return None; # відключити логування запитів у консоль
    
    def send_view(self, view_name = None, layout_name = None) -> None:
        controller_instance = inspect.currentframe().f_back.f_locals['self']
        if layout_name == None:
            layout_name = f'{appconfig.WWWROOT_PATH}/views/_layout.html'
        if view_name == None:
            controller_short_name = controller_instance.__class__.__name__.removesuffix('Controller').lower()
            action_name = inspect.currentframe().f_back.f_code.co_name  # f_back - попередній фрейм (хто викликав)
            view_name = f'{appconfig.WWWROOT_PATH}/views/{controller_short_name}/{action_name}.html'
        if not os.path.isfile(layout_name) or not os.path.isfile(view_name):
            self.send_404()
            return
        for k,v in self.session.items():
            MainHandler.sessions[self.session['id']][k] = v
        self.send_response(200, 'OK')
        self.send_header('Content-Type', 'text/html;')
        for header, value in self.response_headers.items():
            self.send_header(header, value)
        self.end_headers()
        
        with open(view_name, encoding='utf-8') as view:
            view_content = view.read()
            view_data = getattr(controller_instance, 'view_data', None)
            if view_data:
                for k,v in view_data.items():
                    view_content = view_content.replace(k, str(v))
            with open(layout_name, encoding='utf-8') as layout:
                self.wfile.write(
                    layout.read().replace('<!-- RenderBody -->', view_content).encode('utf-8'))

def main():
    if os.path.exists("sessions.json"):
        with open("sessions.json", "r") as f:
            MainHandler.sessions = json.load(f)
    http_server = HTTPServer(('127.0.0.1', 81), MainHandler)
    try:
        print('Server running on port 81')
        http_server.serve_forever()
    except:
        print('Server stopped')
        with open("sessions.json", "w") as f:
            json.dump(MainHandler.sessions, f)
    
if __name__ == '__main__':
    main()
    
'''

Модуль HTTP
Альтернативний підхід до створення серверних програм -
використання власних модулів/пакетів/бібліотек мов
програмування (http.server)
Такі програми складаються з двох блоків:
- запуск/зупинка сервера, підготовка інжекцій, конфігурацій тощо
- обслуговування запитів(слухання) запитів 
Оброблення запитів покладається на клас-нащадок BaseHTTPRequestHandler
Запуск сервера - на об'єкт HTTPServer
Особливості (відмінності від CGI)
- сервер запускається засобами мови (Python), шлях до інтерпретатора
   зазначати не треба, сторонніх серверів також не вимагається.
- серверу не треба, сторонніх серверів також не вимагається.
- серверу потрібен вільний порт для запуску
- метод-обробник не одержує параметрів (типу Request/Response), всі
дані передаються як поля/властивості класу (BaseHTTPRequestHandler)
- тіло відповіді формується записом у поле wfile у бінарному виді
    (рядок треба перевести у байти)
    print() виводить у консоль запуску, у відповідь ці дані не потрапляють
- методи обробника відповідають за методи запиту (do_GET, do_POST, ...)
    і всі запити потрапляють у них (у т.ч. запити на файли, навіть якщо
    файл існує). Задача звернення до файлів має бути вирішена самостійно.
'''

'''
Структура проєкту
Серверні проєкти, які складаються з двох частин - кодової та
статичної, прийнято розподіляти таким чином, щоб прямий доступ
із браузера було обмежено статичними ресурсами. Іншими словами,
пошук файлів (чи інших ресурсів) має бути обемежений окремою
папкою (public, wwwroot, www, static, html).

'''

''' Cookie
Це 
а) заголовки HTTP - пакету, які вимогами стандартів включаються
у всі запити клієнтом.
б) елементи (частіше за все - файли), які зберігає та обслуговує
клієнт (браузер) з метою включення їх до запитів та забезпечення
достатнього часу їх існування (у т.ч. після перезапуску клієнта)

Cookie встановлюються заголовком Set-Cookie: name=value;expires=[DateTime];
path=/  
Якщо треба декілька Cookie, вони передаються окремими заголовками Set-Cookie
Отримавши запит з таким заголовком клієнт (браузер) повинен
зберігти ці дані в усі запити (за шаблоном path) протягом терміну 
(expires) включати заголовок Cookie: name=value; name2=value2; name3=value3
у якому всі Cookie включаються через "; ", тільки імена та значення
(інше ігнорується)
'''