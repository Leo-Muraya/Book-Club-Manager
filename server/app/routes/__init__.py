from flask import Flask
from app.config import Config
from app.extensions import db, jwt, cors

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions first
    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

    # Import routes after extensions
    from app.routes.authentification import auth_bp
    from app.routes.book_clubs import clubs_bp
    from app.routes.Discussions import discussions_bp

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(clubs_bp)
    app.register_blueprint(discussions_bp)

    return app