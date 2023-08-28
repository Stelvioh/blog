from flask import Blueprint, request, jsonify
from service.user_service import UserService
from dto.user_dto import UserDto

user_bp = Blueprint('user', __name__, url_prefix='/user')

user_schema = UserDto()

@user_bp.route('/register', methods=['POST'])
def register():
    # Valida os dados de entrada usando o DTO
    data = request.get_json()
    errors = user_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    # Cria um novo usuário usando os dados validados
    user = UserService.create_user(**data)
    return jsonify({'message': 'User registered successfully!'}), 201


@user_bp.route('/<string:cpf>', methods=['GET'])
def get_user_by_cpf(cpf):
    user = UserService.find_by_cpf(cpf)
    if not user:
        return jsonify({'message': 'User not found!'}), 404

    user_data = user_schema.dump(user)
    return jsonify(user_data)

