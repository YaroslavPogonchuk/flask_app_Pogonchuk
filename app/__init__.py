from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
migrate = Migrate()

def create_app(config_name='config'):
    app = Flask(__name__)
    app.config.from_object(config_name) #налаштування з файлу config.py
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from . import views
        from .posts import post_bp
        from .users import user_bp
        app.register_blueprint(post_bp)
        app.register_blueprint(user_bp)
    return app
