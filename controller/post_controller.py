import json
from flask import Blueprint, request, jsonify
from service.post_service import PostService
from controller.middleware.auth_middleware import token_required, roles_required
from dto.post_dto import PostDto

post_bp = Blueprint('post', __name__, url_prefix='/post')
post_schema = PostDto()


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


@post_bp.route('/create', methods=['POST'])
@token_required
@roles_required('user')
def create_post():
    data = request.get_json()
    errors = post_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    post = PostService.create_post(data['title'], data['content'], data['author_id'])
    return post_schema.dump(post), 201

@post_bp.route('/<int:post_id>', methods=['GET'])
@token_required
def get_post(post_id):
    post = PostService.get_post_by_id(post_id)
    if not post:
        return jsonify({"error": "Post not found"}), 404

    return post_schema.dump(post)

@post_bp.route('/<int:post_id>', methods=['PUT'])
@token_required
@roles_required('user')
def update_post(post_id):
    data = request.get_json()
    post = PostService.update_post(post_id, data['title'], data['content'])
    if not post:
        return jsonify({"error": "Post not found or failed to update"}), 404

    return post_schema.dump(post)

@post_bp.route('/<int:post_id>', methods=['DELETE'])
@token_required
@roles_required('admin')  # Vamos supor que somente admin pode deletar posts.
def delete_post(post_id):
    post = PostService.delete_post(post_id)
    if not post:
        return jsonify({"error": "Post not found or failed to delete"}), 404

    return {"message": "Post deleted successfully"}
