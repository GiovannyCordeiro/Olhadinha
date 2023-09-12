from services.CuponomiaService import CuponomiaService
from services.ZoomService import ZoomService
from services.InterShopService import InterShopService

class FirePlatform:
    logic = {
        'cuponomia': lambda store: CuponomiaService.extract(store),
        'zoom': lambda store: ZoomService.extract(store),
        'intershop': lambda store: InterShopService.extract(store)
    }