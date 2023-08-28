from werkzeug.security import generate_password_hash, check_password_hash
from domain.user import User
from repository.user_repository import UserRepository


class UserService:

    @staticmethod
    def create_user(username, password, email, name, cpf, roles=None):
        hashed_password = generate_password_hash(password, method='sha256')
        user = User(username=username, password=hashed_password, email=email, name=name, cpf=cpf, roles=roles)
        UserRepository.create(user)
        return user

    @staticmethod
    def verify_password(username, password):
        user = UserRepository.find_by_username(username)
        if user and check_password_hash(user.password, password):
            return user
        return None
    
    @staticmethod
    def find_by_cpf(cpf):
        return UserRepository.find_by_cpf(cpf)

