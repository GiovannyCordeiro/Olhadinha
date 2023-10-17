from services.InterShopService import InterShopService
from tests.services.configs.AppContextTests import app_context
class TestClass:
    @app_context
    def test_correctly_data_type(self):
        response = InterShopService.extract("amazon")
        assert type(response) == str

    @app_context
    def test_store_not_existent(self):
        assert InterShopService.extract('loja-da-carabina') == "SNF"