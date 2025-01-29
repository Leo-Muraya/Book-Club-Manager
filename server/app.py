from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from config import config

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from routes.authentification import auth_bp
    from routes.book_clubs import book_clubs_bp
    from routes.books import books_bp
    from routes.Discussions import discussions_bp
    from routes.memberships import memberships_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(book_clubs_bp, url_prefix="/bookclubs")
    app.register_blueprint(books_bp, url_prefix="/books")
    app.register_blueprint(discussions_bp, url_prefix="/discussions")
    app.register_blueprint(memberships_bp, url_prefix="/memberships")

    return app

app = create_app()
