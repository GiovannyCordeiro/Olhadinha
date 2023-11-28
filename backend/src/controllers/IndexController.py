from flask import request, abort
import os

class IndexController:
    def index():
        return {
        'status': 'OK',
        'data': "Welcome to OLHADINHA API"
        }