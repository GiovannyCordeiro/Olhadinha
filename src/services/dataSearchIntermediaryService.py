from models.base.StartDBModel import db
from models.platformsModel import Plataformas

from services.VerifyExistsDataService import VerifyExistsDataService

import json

# data = db.session.execute(db.select(Plataformas)).scalars()
# plataformas = data.all()
# print(plataformas)

# servico intermediador entre consultas do banco e raspagens
class DataSearchIntermediaryService:

    def getAllPlatforms():
        data = db.session.execute(
            db.select(Plataformas)
        ).scalars()
        plataformas = data.all()
        return json.dumps(f"{plataformas[0].nome}")
        # return plataformas

    def save(self):
        allPlatforms = self.getAllPlatforms()
        for platform in allPlatforms:
            data = VerifyExistsDataService.search('amazon', platform.nome)
            # se count(data) for maior que um, retorna o dado para uma estrutura
            # se o count for 0, executa o scrapping e retona o dado
            ''
        'return'