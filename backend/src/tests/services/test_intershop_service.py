from services.InterShopService import InterShopService
from tests.services.configs.AppContextTests import app_context
from tests.services.configs.ValidadeValues import validate_values
class TestClass:
    @app_context
    def test_correctly_data_type(self):
        response = InterShopService.extract("amazon")
        assert type(response) == str

    @app_context
    def test_store_not_existent(self):
        assert InterShopService.extract('loja-da-carabina') == "SNF"
    
    @app_context
    def test_service_response_correcly(self):
        data = InterShopService.extract("Amazon")
        assert validate_values(data)