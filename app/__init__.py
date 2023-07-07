from flask import Flask

def create_app():
    app = Flask(__name__)

    # Blueprints
    from .blueprints.api import api_bp
    app.register_blueprint(api_bp , url_prefix='/api')
    
    return app

app = create_app()

# Routes
from app import admin_views
from app import views
