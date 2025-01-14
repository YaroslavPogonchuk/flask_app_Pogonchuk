from app import db
from datetime import datetime as dt

class Post(db.Model):
    __tablename__='posts'

    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100), nullable=False)
    content=db.Column(db.Text, nullable=False)
    posted=db.Column(db.DateTime, default=dt.now())
    is_active = db.Column(db.Boolean, default=True)
    category=db.Column(db.String(100))
    author=db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Post({self.title})>"