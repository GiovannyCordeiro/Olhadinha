from services.MeuDimDimService import MeuDimDimService
from app import app

class TestClass:
    def test_type(self):
        with app.get_app().app_context():
            assert type(MeuDimDimService.extract('extra')) == float
    
    def test_negative(self):
        with app.get_app().app_context():
            assert MeuDimDimService.extract('extra') >= 0
