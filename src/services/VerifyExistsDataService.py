from models.base.StartDBModel import db
from models.entities.dadosCashbackModel import DadosCashback
from models.entities.platformsModel import Plataformas
from helpers.Plataforms import indexPlatformsDB

from datetime import datetime, timedelta

class VerifyExistsDataService:

    def dateMinusThreeHrs():
        currentTime = datetime.now() 
        threeHrsAgo = currentTime - timedelta(hours=3)
        return threeHrsAgo

    @classmethod
    def search(self, store:str, platform:str)->bool|object:
        threeHrsAgo = self.dateMinusThreeHrs()
        
        data = db.session.execute(
            db.select(DadosCashback).where((DadosCashback.created_at <= threeHrsAgo) &
                (DadosCashback.loja == store) &
                (DadosCashback.plataforma == indexPlatformsDB[f"{platform}"])
            )
        ).scalars()
        allData = data.all()
        if(len(allData) == 0):
            return False
        return allData[0]