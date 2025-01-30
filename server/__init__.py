from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from server.config import config

db = SQLAlchemy()
jwt = JWTManager()

def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        from server.routes import authentification, book_clubs, books, Discussions, memberships  
        app.register_blueprint(authentification.auth_bp)
        app.register_blueprint(book_clubs.book_clubs_bp)
        app.register_blueprint(books.books_bp)
        app.register_blueprint(Discussions.discussions_bp)
        app.register_blueprint(memberships.memberships_bp)

        db.create_all()  

    return app
