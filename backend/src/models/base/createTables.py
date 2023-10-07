from app import app
from models.base.StartDBModel import db
from models.entities.platformsModel import Plataformas

with app.app.app_context():
    db.create_all()
