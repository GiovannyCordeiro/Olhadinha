from services.DataSearchIntermediaryService import DataSearchIntermediaryService
from tests.services.configs.AppContextTests import app_context
class TestClass:
    @app_context
    def test_response_type_getAllPlatforms(self):
        response = DataSearchIntermediaryService.getAllPlatforms()
        assert type(response) == list

    @app_context
    def test_correct_response_getAllPlatforms(self):
        response = DataSearchIntermediaryService.getAllPlatforms()
        assert response == ['cuponomia', 'intershop', 'zoom', 'meudimdim']

    @app_context
    def test_response_type_consultCashbackData(self):
        response = DataSearchIntermediaryService.consultCashbackData('extra')
        assert type(response) == list