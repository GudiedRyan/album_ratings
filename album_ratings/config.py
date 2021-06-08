import os

class BaseConfig:
    SECRET_KEY = os.getenv('AR_SK')
    SQLALCHEMY_DATABASE_URI = os.getenv('AR_SQL_URI')



class DevelopmentConfig(BaseConfig):
    DEBUG = True
    ENV = 'development'