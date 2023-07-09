from models.base.StartDBModel import db

class Plataformas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)

    def __repr__(self):
        return f"Plataformas (id={self.id}, nome={self.nome})"