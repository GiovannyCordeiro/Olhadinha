from services.ZoomService import ZoomService
from tests.services.configs.AppContextTests import app_context
import re

class TestClass:

    def validate_number(self, number):
        regex = "^[-+]?[0-9]*(.[0-9]{1,2})?$"
        match = re.match(regex, number)
        return match is not None

    @app_context
    def test_correct_response_type(self):
        assert type(ZoomService.extract("Amazon")) == str

    @app_context
    def test_store_not_existent(self):
        assert ZoomService.extract("loja-da-carabina") == "SNF"
    
    @app_context
    def test_service_response_correcly(self):
        data = ZoomService.extract("Amazon")
        assert self.validate_number(data)