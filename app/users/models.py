from app import db
from flask_login import UserMixin
from app import login_manager
from datetime import datetime as dt

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ ='user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    img_file = db.Column(db.String(20), nullable=True, default="default.jpg")
    about_me = db.Column(db.Text, nullable=True, default="")
    last_seen = db.Column(db.DateTime, default=dt.now())

    def __repr__(self):
        return f"User('{self.email}')"