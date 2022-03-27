import os

class BaseConfig:
    HOST = os.getenv('APPLICATION_HOST', 'localhost')
    PORT = int(os.getenv('APPLICATION_PORT', '3000'))
    SERVER_NAME = f'{HOST}:{PORT}'
    TESTING = False
    ENV = 'none'
    DEBUG = False

class ProductionConfig(BaseConfig):
    ENV = 'production'

class TestingConfig(BaseConfig):
    ENV = 'production'
    DEBUG = True
    TESTING = True
