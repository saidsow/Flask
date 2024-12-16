from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SECRET_KEY'] = 'your-secret-key'  # Required for session management, flash messages, etc.

    # Register blueprints (routes)
    from .routes import main
    app.register_blueprint(main)

    return app
