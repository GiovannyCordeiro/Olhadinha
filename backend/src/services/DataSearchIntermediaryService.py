from models.base.StartDBModel import db
from models.entities.platformsModel import Plataformas

from services.VerifyExistsDataService import VerifyExistsDataService
from services.FiringPlatformService import FireBotPlatform

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
    def consultCashbackData(cls, store:str) -> dict:
        cls.getAllPlatforms()
        for platform in cls.allPlatforms:
            result = VerifyExistsDataService.search(store, platform)
            if(result == False):
                cls.responseUser[f"{platform}"] = FireBotPlatform.logic[f"{platform}"](store)
                continue
            cls.responseUser[f"{platform}"] = result.porcentagem
        return cls.responseUser
