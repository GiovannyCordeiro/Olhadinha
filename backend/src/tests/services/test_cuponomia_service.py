from services.CuponomiaService import CuponomiaService
from tests.services.configs.AppContextTests import app_context
class TestClass:
    @app_context
    def test_type(self):
        assert type(CuponomiaService.extract('Amazon')) == str
    
    @app_context
    def test_store_not_existent(self):
        assert CuponomiaService.extract('loja-da-carabina') == "SNF"
