from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from sqlalchemy.orm import DeclarativeBase
from flask_login import LoginManager


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app(config_name="../config.py"):
    app = Flask(__name__, static_folder='static')
    app.config.from_pyfile(config_name)

    db.init_app(app)
    migrate.init_app(app, db)

    bcrypt.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = "users.login"
    login_manager.login_message = "Please log in access this page."
    login_manager.login_message_category = "warning"

    with app.app_context():
        from . import views

        from .users import user_bp
        app.register_blueprint(user_bp)

        from .posts import post_bp
        app.register_blueprint(post_bp)

    return app