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
                "test": VerifyExistsDataService.search()
                # 'Cuponomia': CuponomiaService.extract(store),
                # 'Zoon': ZoomService.extract(store)
            }
        }