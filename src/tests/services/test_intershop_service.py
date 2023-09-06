from app import app
from services.InterShopService import InterShopService

class TestClass:
    def test_correctly_data_type(self):
        with app.get_app().app_context():
            response = InterShopService.extract("amazon")
            assert type(response) == float
    
    def test_positive_numbers(self):
        with app.get_app().app_context():
            response = InterShopService.extract("amazon")
            assert response >= 0