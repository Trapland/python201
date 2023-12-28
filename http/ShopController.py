from http.server import BaseHTTPRequestHandler
import inspect
import appconfig
import os
import dao

class ShopController:
    
    def __init__(self, handler: BaseHTTPRequestHandler) -> None:
        self.short_name = self.__class__.__name__.lower().replace('controller','')
        self.handler = handler
        
        
    def index(self):
        self.view_data = {
            "products": dao.Products().get_all()
        }
        self.handler.send_view() # action_name = inspect.currentframe().f_code.co_name
        
    def cart(self):
        self.handler.send_view() # action_name = inspect.currentframe().f_code.co_name
        
    def return_view(self, action_name: str = None):
        self.handler.send_view()