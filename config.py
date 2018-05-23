import os

class Config:
    SECRET_KEY = 'CANSSIDLE12'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://canssidle:judycharles@localhost/pitch'


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options ={"production":ProdConfig,"default":DevConfig}


