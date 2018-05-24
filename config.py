import os

class Config:
    SECRET_KEY = 'CANSSIDLE12'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://canssidle:judycharles@localhost/pitch'
    SIMPLEMDE_JS_LIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options ={"production":ProdConfig,"development":DevConfig}


