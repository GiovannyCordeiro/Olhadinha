import os

SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = os.getenv('DBCONNECTION')

CORS_ORIGINS = [os.getenv('ORIGIN_ALLOWED')]

SQLALCHEMY_TRACK_MODIFICATIONS = False