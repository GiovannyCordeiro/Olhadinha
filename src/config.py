import os

SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

# SQLALCHEMY_DATABASE_URI = os.getenv('DBCONNECTION')

SQLALCHEMY_DATABASE_URI = ${{ secrets.DB_CONECTION }}


SQLALCHEMY_TRACK_MODIFICATIONS = False