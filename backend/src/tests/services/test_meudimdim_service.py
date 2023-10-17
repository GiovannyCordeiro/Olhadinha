from services.MeuDimDimService import MeuDimDimService
from tests.services.configs.AppContextTests import app_context
class TestClass:
    @app_context
    def test_type(self):
        assert type(MeuDimDimService.extract('extra')) == str
    
    @app_context
    def test_store_not_existent(self):
        assert MeuDimDimService.extract('amazon') == "SNF"
