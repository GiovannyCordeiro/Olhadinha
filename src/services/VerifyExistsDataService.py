from models.base.StartDBModel import db
from models.dadosCashbackModel import DadosCashback
from models.platformsModel import Plataformas
from helpers.Plataforms import allPlataforms

from datetime import datetime, timedelta

class VerifyExistsDataService:

    def dateMinusThreeHrs():
        currentTime = datetime.now() 
        threeHrsAgo = currentTime - timedelta(hours=3)
        return threeHrsAgo

    @classmethod
    def search(self, store:str, platform:str)->list:
        threeHrsAgo = self.dateMinusThreeHrs()
        
        data = db.session.execute(
            db.select(DadosCashback).where((DadosCashback.created_at >= threeHrsAgo) &
                (DadosCashback.loja == store) &
                (DadosCashback.plataforma == allPlataforms[f"{platform}"])
            )
        ).scalars()
        allData = data.all()

        print("data", allData)
        return allData