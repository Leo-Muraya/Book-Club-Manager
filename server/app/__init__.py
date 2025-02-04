from flask import Flask
from app.config import Config
from app.extensions import db, jwt, cors
from flask_cors import CORS

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

    # Import routes after extensions
    from app.routes.authentification import auth_bp
    from app.routes.book_clubs import clubs_bp
    from app.routes.Discussions import discussions_bp

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(clubs_bp, url_prefix='/api/clubs')
    app.register_blueprint(discussions_bp, url_prefix='/api/discussions')

    return app