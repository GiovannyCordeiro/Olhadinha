from services.DataSearchIntermediaryService import DataSearchIntermediaryService
from app import app

class TestClass:
    def test_response_type_getAllPlatforms(self):
        with app.get_app().app_context():
            response = DataSearchIntermediaryService.getAllPlatforms()
            assert type(response) == list

    def test_correct_response_getAllPlatforms(self):
        with app.get_app().app_context():
            response = DataSearchIntermediaryService.allPlatforms
            assert response == ['cuponomia', 'intershop', 'zoom', 'meudimdim']

    def test_response_type_consultCashbackData(self):
        with app.get_app().app_context():
            response = DataSearchIntermediaryService.consultCashbackData('amazon')
            assert type(response) == dict