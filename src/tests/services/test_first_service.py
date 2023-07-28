from services.first_service import TestService
from app import App

def test_index():
    app = App().create_app()
    app.app_context().push()
    assert TestService.index() == [
		"meliuz",
		"cuponomia",
		"intershop",
        "zoom"
	]