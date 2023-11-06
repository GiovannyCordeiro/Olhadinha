from models.base.StartDBModel import db
from models.entities.platformsModel import Plataformas

from services.VerifyExistsDataService import VerifyExistsDataService
from services.FiringPlatformService import FireBotPlatform

from flask import jsonify

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

    def consultCashbackData( store:str) -> dict:
        responseUser = []
        allPlatforms = DataSearchIntermediaryService.getAllPlatforms()
        print(allPlatforms)
        for platform in allPlatforms:
            result = VerifyExistsDataService.search(store, platform)
            if(result == False):
                responseUser.append({
                'namePlatform': platform,
                'percentage': FireBotPlatform.logic[f"{platform}"](store)
                })
                continue
            responseUser.append({
                'namePlatform': platform,
                'percentage': result.porcentagem
            })
        return responseUser
