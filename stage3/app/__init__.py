from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Configure logging
    #logging.basicConfig(filename=app.config['LOG_FILE'], level=logging.INFO)

    from .views import main
    app.register_blueprint(main)

    return app