from flask_caching import Cache
from app import config
from app.services.logging import create_logger

cache = Cache(config=config.BASE_CACHE_CONFIG)
logger = create_logger()