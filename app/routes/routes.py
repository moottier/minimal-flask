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

@api.route('/posts', methods=['GET'])
def get():
    tags = request.args.get('tags') or ''
    tags = services.parse_tags(tags)

    sort_by = request.args.get('sortBy') or 'id'
    direction = request.args.get('direction') or 'asc'

    if not tags :
        return {'error': 'Tags parameter is required'}, 400

    if not services.validate_sort_by(sort_by):
        return {'error': 'sortBy parameter is invalid'}, 400

    if not services.validate_direction(direction):
        return {'error': 'direction parameter is invalid'}, 400

    return services.process_request(tags, sort_by, direction), 200