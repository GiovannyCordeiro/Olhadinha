from models.base.StartDBModel import db
from models.entities.platformsModel import Plataformas
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func

class DadosCashback(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    porcentagem = db.Column(db.String)
    plataforma = db.Column(db.Integer, ForeignKey(Plataformas.id))
    loja = db.Column(db.String)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"DadosCashback (id={self.id}, porcentagem={self.porcentagem})"