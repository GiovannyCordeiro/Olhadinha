from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Inserttable(db.Model):
    __tablename__ = 'inserttable'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    machineid = db.Column(db.Integer, primary_key=False)
    stateid = db.Column(db.Integer, primary_key=False)
    speed = db.Column(db.Integer, nullable=False)
    statechange = db.Column(db.Integer, nullable=False)
    unixtime = db.Column(db.Integer, nullable=False)
    extras = db.Column(db.String(80), nullable=False)
    state = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<machineid %r>' % self.machineid
