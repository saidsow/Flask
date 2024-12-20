from flask import Flask
from flask_app.plotlydash import create_dash_app

def create_app():
    app = Flask(__name__)
    app.secret_key = 'key'  # Replace with a strong secret key
    
    # Register Dash app
    create_dash_app(app)

    with app.app_context():
        # Import parts of our application
        from . import routes

    return app

