class Config(object):
    """Base config."""
    SECRET_KEY = "qeqwrwe1231weerw"
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    DEBUG = True

class Production(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
   
class Development(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True