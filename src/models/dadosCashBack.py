from models.base.StartDBModel import db
from models.platformsModel import Plataformas
import sqlalchemy as sa
from sqlalchemy import func

class dadosCashback(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    porcentagem = sa.Column(sa.Text)
    plataforma = sa.Column(sa.ForeignKey(Plataformas.id))
    loja = sa.Column(sa.Text)
    created_at = sa.Column(sa.TIMESTAMP, server_default=func.now())

    def __repr__(self):
        return f"Dados Cashback (id={self.id}, porcentagem={self.porcentagem}, plataforma={self.plataforma}, loja={self.loja}, created_at={self.created_at})"