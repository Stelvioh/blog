from domain.user import User, db

class UserRepository:

    @staticmethod
    def create(user):
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def find_by_username(username):
        return User.query.filter_by(username=username).first()
    
    @staticmethod
    def find_by_cpf(cpf):
        return User.query.filter_by(cpf=cpf).first()
