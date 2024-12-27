from flask import Flask
from flask_cors import CORS
from app.api.routes import bp

def create_app():
    app = Flask(__name__)
    
    # Configure CORS for frontend
    CORS(app, resources={
        r"/api/*": {
            "origins": ["http://localhost:3000", "http://127.0.0.1:3000"],
            "methods": ["GET", "POST", "OPTIONS"],
            "allow_headers": ["Content-Type", "Accept"],
            "supports_credentials": True
        }
    })
    
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
    app.register_blueprint(bp)
    return app