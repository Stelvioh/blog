import json
from flask import Blueprint, request, jsonify
from service.post_service import PostService

post_bp = Blueprint('post', __name__, url_prefix='/post')

@post_bp.route('', methods=['GET'])
def get_all_posts():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    order_by = request.args.get('order_by', 'id', type=str)
    direction = request.args.get('direction', 'asc', type=str)
    filters_str = request.args.get('filters', None)

    filters = json.loads(filters_str) if filters_str else None

    result = PostService().get_all_posts(page, per_page, order_by, direction, filters)
    return jsonify(result)

# Adicione aqui outros endpoints relacionados a postagens, como adicionar uma nova postagem, editar, excluir, etc.
