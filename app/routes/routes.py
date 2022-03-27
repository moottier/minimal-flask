from flask import Blueprint, request
from app.services import services

api = Blueprint(
    name = 'api', 
    import_name=__name__,
    url_prefix='/api',
)

@api.route('/ping', methods=['GET'])
def ping():
    return {'success': True}, 200

@api.route('/<item>', methods=['GET'])
def get(item):
    pass