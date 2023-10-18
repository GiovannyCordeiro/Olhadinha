from services.CuponomiaService import CuponomiaService
from tests.services.configs.AppContextTests import app_context
from tests.services.configs.ValidadeValues import validate_values
class TestClass:
    @app_context
    def test_type(self):
        assert type(CuponomiaService.extract('Amazon')) == str
    
    @app_context
    def test_store_not_existent(self):
        assert CuponomiaService.extract('loja-da-carabina') == "SNF"

    @app_context
    def test_service_response_correcly(self):
        data = CuponomiaService.extract("Amazon")
        assert validate_values(data)
