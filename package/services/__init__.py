from flask_caching import Cache
from package import config

cache = Cache(config=config.BASE_CACHE_CONFIG)
