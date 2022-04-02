import os
from pathlib import Path

BASE_CACHE_CONFIG = {'CACHE_TYPE': 'SimpleCache'}

class BaseFlaskConfig:
    HOST = os.getenv('APPLICATION_HOST', 'localhost')
    PORT = int(os.getenv('APPLICATION_PORT', '3000'))
    SERVER_NAME = f'{HOST}:{PORT}'
    TESTING = False
    ENV = 'none'
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(BaseFlaskConfig):
    ENV = 'production'
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    PORT = 3000
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{Path(__file__).parents[0] / "prod.db"}'

class DevelopmentConfig(BaseFlaskConfig):
    ENV = 'development'
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = False
    PORT = 3000
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{Path(__file__).parents[0] / "dev.db"}'

class TestingConfig(BaseFlaskConfig):
    ENV = 'testing'
    FLASK_ENV = 'testing'
    DEBUG = True
    TESTING = True
    PORT = 3000
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{Path(__file__).parents[0] / "test.db"}'

config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig,
}
