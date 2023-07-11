import json
from sqlalchemy import select
from models.base.StartDBModel import db
from models.platformsModel import Plataformas

class TestService:
    def index():
        allPlatforms = db.session.query(Plataformas).all()
        
        namePlatforms = []
        for platforms in allPlatforms:
            namePlatforms.append(platforms.nome)
        
        return namePlatforms
    
    def sumNum(number):
        return number + 10