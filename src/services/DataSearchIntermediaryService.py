from models.base.StartDBModel import db
from models.entities.platformsModel import Plataformas

from services.VerifyExistsDataService import VerifyExistsDataService

from services.CuponomiaService import CuponomiaService
from services.ZoomService import ZoomService
from services.InterShopService import InterShopService

class DataSearchIntermediaryService:
    allPlatforms = []
    responseUser = {}

    @classmethod
    def getAllPlatforms(cls):
        data = db.session.execute(
            db.select(Plataformas)
        ).scalars()
        responseDB = data.all()
        for value in responseDB:
            cls.allPlatforms.append(value.nome)
        return cls.allPlatforms

    @classmethod
    def consultCashbackData(cls, store:str)->dict:
        cls.getAllPlatforms()
        for platform in cls.allPlatforms:
            result = VerifyExistsDataService.search(store, platform)
            if(result == False):
                if(platform == 'cuponomia'):
                    cls.responseUser[f"{platform}"] = CuponomiaService.extract(store)
                if(platform == 'zoom'):
                    cls.responseUser[f"{platform}"] = ZoomService.extract(store)
                if(platform == 'intershop'):
                    cls.responseUser[f"{platform}"] = InterShopService.extract(store)
                continue
            cls.responseUser[f"{platform}"] = result.porcentagem
        return cls.responseUser
