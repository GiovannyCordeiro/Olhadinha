from services.CuponomiaService import CuponomiaService
from services.ZoomService import ZoomService
from services.SearchDataService import SearchDataConsult

class PlatformController:
    def searchPlatforms(store):
        # data = SearchDataConsult.meta(store)
        return {
            'status': 'OK',
            'cashbackPlatfomrs': {
                'Cuponomia': CuponomiaService.extract(store),
                'Zoon': ZoomService.extract(store)
            }
        } 