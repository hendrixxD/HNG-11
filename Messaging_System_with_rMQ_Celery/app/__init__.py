
from flask import Flask
from .views import main
from .config import Config
from .tasks import make_celery

def create_app():
    """
    Create and configure the Flask application.
    
    This function:
    1. Creates a Flask app instance
    2. Loads configuration from Config object
    3. Initializes Celery for asynchronous tasks
    4. Registers the main blueprint
    
    Returns:
        tuple: A tuple containing the Flask app and Celery instances
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Celery
    celery = make_celery(app)
    
    # registerers blueprint
    app.register_blueprint(main)
    return app, celery
