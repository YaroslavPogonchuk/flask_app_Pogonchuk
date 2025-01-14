import os

SECRET_KEY = "dwqe124sd59D23"
FLASK_DEBUG = 1
SQLALCHEMY_DATABASE_URI = 'sqlite:///data.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOAD_FOLDER = os.path.join(os.getcwd(),'app','users', 'static', 'images', 'account')