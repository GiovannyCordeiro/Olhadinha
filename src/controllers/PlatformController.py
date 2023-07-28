from services.CuponomiaService import CuponomiaService
from services.ZoomService import ZoomService
from services.VerifyExistsDataService import VerifyExistsDataService

class PlatformController:

    @classmethod
    def searchPlatforms(cls,store):
        return {
            'status': 'OK',
            'cashbackPlatfomrs': {
                "Lorem ipsum": "DOLOR",
                "test": f"{VerifyExistsDataService.search(store,'meliuz')}"
                # 'Cuponomia': CuponomiaService.extract(store),
                # 'Zoon': ZoomService.extract(store)
            }
        }