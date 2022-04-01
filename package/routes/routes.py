from flask import Blueprint, current_app
from package.services import cache

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
def get(item):
    print("APP ENV:", current_app.config['ENV'])
    print("APP DEBUG:", current_app.config['DEBUG'])
    print("APP TESTING:", current_app.config['TESTING'])
    return {'success': item}, 200