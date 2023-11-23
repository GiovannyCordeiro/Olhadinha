from models.base.StartDBModel import db
from models.entities.platformsModel import Plataformas

from services.VerifyExistsDataService import VerifyExistsDataService
from services.FiringPlatformService import FireBotPlatform
from helpers.URLsScrapping import ULRsScrapping

class DataSearchIntermediaryService:

    @staticmethod
    def getAllPlatforms():
        allPlatforms = []
        data = db.session.execute(
            db.select(Plataformas)
        ).scalars()
        responseDB = data.all()
        for value in responseDB:
            allPlatforms.append(value.nome)
        return allPlatforms

    def consultCashbackData(store:str) -> dict:
        responseUser = []
        allPlatforms = DataSearchIntermediaryService.getAllPlatforms()
        for platform in allPlatforms:
            result = VerifyExistsDataService.search(store, platform)
            if(result == False):
                responseUser.append({
                'namePlatform': platform,
                'morePlatform': {
                    'percentage': FireBotPlatform.logic[f"{platform}"](store),
                    'link': ULRsScrapping.logic[f"{platform}"](store.lower())
                }
                })
                continue
            responseUser.append({
                'namePlatform': platform,
                'morePlatform': {
                    'percentage': result.porcentagem,
                    'link': ULRsScrapping.logic[f"{platform}"](store.lower())
                }
            })
        return responseUser
