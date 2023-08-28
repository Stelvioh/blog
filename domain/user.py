from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    roles = db.Column(db.String(80), nullable=True)  # Apenas uma sugestão, isso pode ser modificado conforme suas necessidades

    # Se necessário, atualize o construtor e outros métodos para lidar com os novos campos
    def __init__(self, username, password, email, name, cpf, roles=None):
        self.username = username
        self.password = password
        self.email = email
        self.name = name
        self.cpf = cpf
        self.roles = roles
