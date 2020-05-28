from BookProject import db, login
from flask_login import UserMixin
from datetime import datetime

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class Review(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), primary_key=True)
    date = db.Column( db.DateTime, default=datetime.utcnow)
    rating = db.Column( db.Integer, nullable=True)
    comment = db.Column(db.String(500), nullable=True)
    user = db.relationship('User', backref="reviews", lazy= True)
    book = db.relationship('Book', backref="reviews", lazy= True)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    picture = db.Column(db.String(100), default="default.png")
    books= db.relationship('Book',secondary="review", backref="users", lazy=True)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(100), unique=True, nullable=False)
    title = db.Column(db.String(100),nullable=False)
    author = db.Column(db.String(40), nullable=False)
    year =db.Column(db.Integer, nullable=False)