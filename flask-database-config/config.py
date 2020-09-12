from os import environ, path
from dotenv import load_dotenv
import os
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Base config."""
    SECRET_KEY = "worldisbest"
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

class Production(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
   
class Development(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True