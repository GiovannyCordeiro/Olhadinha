from models.entities.dadosCashbackModel import DadosCashback
from models.base.StartDBModel import db
from app import app

platformas = [
    DadosCashback(porcentagem='3', plataforma=1, loja="AliExpress"),
    DadosCashback(porcentagem='5', plataforma=2, loja="Kabum"),
    DadosCashback(porcentagem='1', plataforma=4, loja="Amazom")
]

with app.app.app_context():
    db.session.add_all(platformas)
    db.session.commit()
