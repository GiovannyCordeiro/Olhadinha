import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = f"postgresql://{os.environ['USERDB']}:{os.environ['PASSWORDDB']}@{os.environ['LOCALDB']}/{os.environ['NAMEDB']}"

SQLALCHEMY_TRACK_MODIFICATIONS = False