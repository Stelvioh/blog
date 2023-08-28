import os
from flask import Flask
from domain.user import db
from controller.user_controller import user_bp
from controller.post_controller import post_bp
from controller.auth_controller import auth_bp
from flask_jwt_extended import JWTManager
import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config.config[config_name])

    db.init_app(app)
    jwt = JWTManager(app)
    
    app.register_blueprint(user_bp)
    app.register_blueprint(post_bp)
    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all()    
    
    return app

if __name__ == "__main__":
    env = os.environ.get('FLASK_ENV', 'default')
    app = create_app(env)
    app.run()
