import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@192.168.0.102:5433/public"

SQLALCHEMY_TRACK_MODIFICATIONS = False