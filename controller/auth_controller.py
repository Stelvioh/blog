from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from service.user_service import UserService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])

def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    user = UserService.verify_password(username, password)
    if not user:
        return jsonify({"msg": "Bad username or password"}), 401

    # Usando roles do objeto user para criar o token
    access_token = create_access_token(identity=username, additional_claims={"roles": user.roles})
    return jsonify(access_token=access_token), 200
