from app import app
from models.base.StartDBModel import db

with app.app_context():
    db.create_all()
