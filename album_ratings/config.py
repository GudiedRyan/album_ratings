import os

class BaseConfig:
    SECRET_KEY = os.getenv('AR_SK')
    SQLALCHEMY_DATABASE_URI = os.getenv('AR_SQL_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    FLASK_ENV = 'development'


class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'

class TestingConfig(BaseConfig):
    TESTING = True