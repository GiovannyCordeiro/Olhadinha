from services.CuponomiaService import CuponomiaService
from app import app

class TestClass:
    def test_type(self):
        with app.get_app().app_context():
            assert type(CuponomiaService.extract('Amazon')) == int
    
    def test_negative(self):
        with app.get_app().app_context():
            assert CuponomiaService.extract('Amazon') >= 0
