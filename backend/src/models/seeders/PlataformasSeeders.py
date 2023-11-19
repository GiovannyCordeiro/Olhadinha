from models.entities.platformsModel import Plataformas
from models.entities.dadosCashbackModel import DadosCashback
from models.base.StartDBModel import db
from app import app
from helpers.Plataforms import indexPlatformsDB

platformas = [
    Plataformas(nome="cuponomia", id = indexPlatformsDB['cuponomia']),
    Plataformas(nome="intershop", id = indexPlatformsDB['intershop']),
    Plataformas(nome="zoom", id = indexPlatformsDB['zoom']),
    Plataformas(nome="meudimdim", id = indexPlatformsDB['meudimdim'])
]

with app.app_context():
    db.session.add_all(platformas)
    db.session.commit()
