from flask import Flask

app = Flask(__name__, static_folder='static')
app.config.from_pyfile("../config.py")

from . import views

from .users import user_bp
app.register_blueprint(user_bp)

from .posts import post_bp
app.register_blueprint(post_bp)