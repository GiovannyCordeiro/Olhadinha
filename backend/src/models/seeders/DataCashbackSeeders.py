from models.entities.dadosCashbackModel import DadosCashback
from models.base.StartDBModel import db
from app import app
from helpers.Plataforms import indexPlatformsDB

platformas = [
    DadosCashback(porcentagem='3', plataforma=indexPlatformsDB['intershop'], loja="AliExpress"),
    DadosCashback(porcentagem='5', plataforma=indexPlatformsDB['cuponomia'], loja="Kabum"),
    DadosCashback(porcentagem='1', plataforma=indexPlatformsDB['zoom'], loja="Amazom")
]

with app.app_context():
    db.session.add_all(platformas)
    db.session.commit()
