import os
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from routes.blueprint import blueprint
from models.base.StartDBModel import db

load_dotenv()

class App:
    def __init__(self):
        self.app = self.create_app()

    def create_app(self):
        app = Flask(__name__)
        app.config.from_object('config')
        db.init_app(app)
        return app
    
    def run(self):
        self.app.register_blueprint(blueprint, url_prefix='/')
        if __name__ == '__main__':
            self.app.run(host=os.environ['HOST'], port=os.environ['PORT'], debug=True)

    def get_app(self):
        return self.app

app = App()
app.run()