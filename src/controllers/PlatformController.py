from services.CuponomiaService import CuponomiaService
from services.ZoomService import ZoomService

class PlatformController:
    def searchPlatforms(store):
        return {
            'status': 'OK',
            'cashbackPlatfomrs': {
                'Cuponomia': CuponomiaService.extract(store),
                'Zoon': ZoomService.extract(store)
            }
        }