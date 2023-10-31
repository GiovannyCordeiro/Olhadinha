import os
from flask import Flask
from routes.blueprint import blueprint
from models.base.StartDBModel import db
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
CORS(app)

app.register_blueprint(blueprint, url_prefix='/')

if __name__ == '__main__':
    app.run(host=os.environ['HOST'], port=os.environ['PORT'], debug=True)