from flask import Blueprint, current_app
from app.services import cache

api = Blueprint(
    name = 'api', 
    import_name=__name__,
    url_prefix='/api',
)

@api.route('/ping', methods=['GET'])
@cache.cached(timeout=10)
def ping():
    return {'success': f"{current_app.config['HOST']}:{current_app.config['PORT']}"}, 200

@api.route('/<item>', methods=['GET'])
@cache.cached(timeout=10, query_string=True)
def get(item):
    return {'success': item}, 200