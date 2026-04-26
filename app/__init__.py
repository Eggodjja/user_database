from flask import Flask 
from .extensions import db, migrate, csrf
from .config import Config
from .routes.user import user


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    app.register_blueprint(user)
    
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    
    with app.app_context():
        db.create_all()
    return app
