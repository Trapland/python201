#Функції
def pair():     # def - ключове слово для оголошення функції
    return 1,2  # повернення значення (кортеж)
                # Рекомедація - залишати щонайменше 
                # два порожні рядки
def hello() -> str:         # Опціональне зазначення типу повернення ф-ції
    x = 20                  # Локальна змінна, яка "перекриває" глобальну
    return "Hello, World %d" % (x)   # виведе 20, але глобальна змінна не зміниться


def change_x() -> None:
    global x            # декларація того, що під "х" розуміється саме
    x = 20              # глобальна змінна, її нове значення зафіксується


def main() -> None:
    print(hello())
    x,y = pair()
    print(x)
    change_x()
    print(x)
    
    
# Одне з використань функцій - створення "точки входження"

if __name__ == '__main__' : main()