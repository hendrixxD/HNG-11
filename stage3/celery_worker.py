from app import create_app
from app.tasks import celery

"""
This script initializes the Flask app and Celery instance for the worker process.
"""
app, celery = create_app()
app.app_context().push()
