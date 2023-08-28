from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import get_jwt, jwt_required

def token_required(f):
    @jwt_required()
    @wraps(f)
    def decorated(*args, **kwargs):
        # Com a anotação @jwt_required(), se o token não for válido, o próprio Flask-JWT-Extended irá retornar uma resposta de erro.
        # Se passar por esta função, sabemos que o token é válido.
        return f(*args, **kwargs)
    return decorated

def roles_required(*required_roles):
    def decorator(f):
        @jwt_required()
        @wraps(f)
        def decorated_function(*args, **kwargs):
            claims = get_jwt()
            user_roles = claims.get("roles", [])

            for required_role in required_roles:
                if required_role not in user_roles:
                    return jsonify({"error": f"You need the {required_role} role to access this resource!"}), 403

            return f(*args, **kwargs)
        
        return decorated_function
    return decorator
