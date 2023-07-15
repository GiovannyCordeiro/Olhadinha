from services.CuponomiaService import CuponomiaService

class PlatformController:
    def searchPlatforms(store):
        return {
            'status': 'OK',
            'cashbackPlatfomrs': {
                'cuponomia': CuponomiaService.extract(store)
            }
        }