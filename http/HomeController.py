from http.server import BaseHTTPRequestHandler
import inspect
import appconfig
import os

class HomeController:
    
    def __init__(self, handler: BaseHTTPRequestHandler) -> None:
        # self.short_name = self.__class__.__name__.lower().replace('controller','')
        self.handler = handler
        
        
    def index(self):
        self.handler.session['data'] = 'HomeController'
        self.view_data = {
            "@session-timestamp": self.handler.session['timestamp']
        }
        self.handler.send_view()
        
    def about(self):
        self.handler.send_view()
        
    def privacy(self):
        self.handler.send_view()
        
    def return_view(self, action_name):
        self.handler.send_view()