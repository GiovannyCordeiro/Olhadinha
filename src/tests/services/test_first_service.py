from services.first_service import TestService

def test_sum():
    assert TestService.index() == "Testing service"