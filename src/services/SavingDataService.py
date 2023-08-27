from models.base.StartDBModel import db

from models.entities.dadosCashbackModel import DadosCashback

class SavingDataService:

    @staticmethod
    def save(store:str, idPlatform:int, cashback:str):
        newData = DadosCashback(loja=store, plataforma=idPlatform, porcentagem=cashback)
        db.session.add(newData)
        db.session.commit()
