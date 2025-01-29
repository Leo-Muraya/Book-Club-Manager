from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from routes.authentification import auth_bp
from routes.book_clubs import book_clubs_bp
from routes.books import books_bp
from routes.memberships import memberships_bp
from routes.Discussions import discussions_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book_club.db'
app.config['JWT_SECRET_KEY'] = 'supersecretkey'

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(book_clubs_bp, url_prefix='/api')
app.register_blueprint(books_bp, url_prefix='/api')
app.register_blueprint(memberships_bp, url_prefix='/api')
app.register_blueprint(discussions_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
