from services.CuponomiaService import CuponomiaService

class TestClass:
    def test_type(self):
        assert type(CuponomiaService.extract('Amazon')) == int
    
    def test_negative(self):
        assert CuponomiaService.extract('Amazon') >= 0
