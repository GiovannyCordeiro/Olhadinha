from services.CuponomiaService import CuponomiaService
from app import app

class TestClass:
    def test_type(self):
        with app.get_app().app_context():
            assert type(CuponomiaService.extract('Amazon')) == str
    
    def test_store_not_existent(self):
        with app.get_app().app_context():
            assert CuponomiaService.extract('loja-da-carabina') == "SNF"
