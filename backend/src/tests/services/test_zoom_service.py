from services.ZoomService import ZoomService
from tests.services.configs.AppContextTests import app_context
from tests.services.configs.ValidadeValues import validate_values
class TestClass:

    @app_context
    def test_correct_response_type(self):
        assert type(ZoomService.extract("Amazon")) == str

    @app_context
    def test_store_not_existent(self):
        assert ZoomService.extract("loja-da-carabina") == "SNF"
    
    @app_context
    def test_service_response_correcly(self):
        data = ZoomService.extract("Amazon")
        assert validate_values(data)