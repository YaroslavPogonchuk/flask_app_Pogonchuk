from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
migrate = Migrate()

def create_app(config_name="../config.py"):
    app = Flask(__name__, static_folder='static')
    app.config.from_pyfile(config_name)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from . import views

        from .users import user_bp
        app.register_blueprint(user_bp)

        from .posts import post_bp
        app.register_blueprint(post_bp)

    return app