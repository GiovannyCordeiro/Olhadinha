from models.entities.platformsModel import Plataformas
from models.entities.dadosCashbackModel import DadosCashback
from models.base.StartDBModel import db
from app import app

platformas = [
    Plataformas(nome="meliuz"),
    Plataformas(nome="cuponomia"),
    Plataformas(nome="intershop"),
    Plataformas(nome="zoom")
]

with app.app.app_context():
    db.session.add_all(platformas)
    db.session.commit()
