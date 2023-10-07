from services.MeuDimDimService import MeuDimDimService
from app import app

class TestClass:
    def test_type(self):
        with app.get_app().app_context():
            assert type(MeuDimDimService.extract('extra')) == str
    
    def test_store_not_existent(self):
        with app.get_app().app_context():
            assert MeuDimDimService.extract('amazon') == "SNF"
