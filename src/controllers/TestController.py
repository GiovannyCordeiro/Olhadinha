import json
# from models.machine import db
from services.first_service import TestService

class TestController:
    def index():
        return {
        'status': 'OK',
        'data': TestService.index()
        }