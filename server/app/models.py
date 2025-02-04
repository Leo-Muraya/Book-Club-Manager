from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    
    clubs = db.relationship('Membership', back_populates='user')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class BookClub(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    members = db.relationship('Membership', back_populates='club')
    books = db.relationship('Book', back_populates='club')
    discussions = db.relationship('Discussion', back_populates='club')

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100))
    club_id = db.Column(db.Integer, db.ForeignKey('book_club.id'))
    
    club = db.relationship('BookClub', back_populates='books')

class Discussion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    club_id = db.Column(db.Integer, db.ForeignKey('book_club.id'))
    
    club = db.relationship('BookClub', back_populates='discussions')

class Membership(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    club_id = db.Column(db.Integer, db.ForeignKey('book_club.id'), primary_key=True)
    role = db.Column(db.String(50))
    
    user = db.relationship('User', back_populates='clubs')
    club = db.relationship('BookClub', back_populates='members')