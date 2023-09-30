from app import app
from services.InterShopService import InterShopService

class TestClass:
    def test_correctly_data_type(self):
        with app.get_app().app_context():
            response = InterShopService.extract("amazon")
            assert type(response) == str

    def test_store_not_existent(self):
        with app.get_app().app_context():
            assert InterShopService.extract('loja-da-carabina') == "SNF"