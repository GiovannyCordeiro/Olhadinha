from models.base.StartDBModel import db
from models.platformsModel import Plataformas

from services.VerifyExistsDataService import VerifyExistsDataService

class DataSearchIntermediaryService:
    allPlataforms = []
    responseUser = {}

    @classmethod
    def getAllPlatforms(cls):
        data = db.session.execute(
            db.select(Plataformas)
        ).scalars()
        responseDB = data.all()
        for value in responseDB:
            cls.allPlataforms.append(value.nome)
        return cls.allPlataforms

    @classmethod
    def consultCashbackData(cls):
        cls.getAllPlatforms()
        for platform in cls.allPlataforms:
            result = VerifyExistsDataService.search('amazon', platform)
            if(result == False):
                ''
            # se count(data) for maior que um, retorna o dado para uma estrutura
            # se o count for 0, executa o scrapping e retona o dado
        return 'return'