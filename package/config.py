import os

BASE_CACHE_CONFIG = {'CACHE_TYPE': 'SimpleCache'}

class BaseFlaskConfig:
    HOST = os.getenv('APPLICATION_HOST', 'localhost')
    PORT = int(os.getenv('APPLICATION_PORT', '3000'))
    SERVER_NAME = f'{HOST}:{PORT}'
    TESTING = False
    ENV = 'none'
    DEBUG = False

class ProductionConfig(BaseFlaskConfig):
    ENV = 'production'
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    PORT = 3000

class TestingConfig(BaseFlaskConfig):
    ENV = 'development'
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    PORT = 3000

config = {
    'production': ProductionConfig,
    'development': TestingConfig,
    'testing': TestingConfig,
    'default': TestingConfig,
}