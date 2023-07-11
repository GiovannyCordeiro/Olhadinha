from services.first_service import TestService

def test_index():
    assert TestService.sumNum(10) == 20