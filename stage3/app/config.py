import os
from dotenv import load_dotenv

load_dotenv()

"""
Credentials configurations for  rabitmq and smtp
"""
class Config:
    """
    Configuration class for the application.

    This class loads environment variables for:
    - RabbitMQ connection
    - Celery configuration
    - Logging
    - SMTP server settings

    All configuration variables are loaded from a .env file.
    """
    # RabbitMQ Configurations
    USER = os.getenv('RABBITMQ_USER')
    PASS = os.getenv('RABBITMQ_PASS')
    HOST = os.getenv('RABBITMQ_HOST')
    PORT = os.getenv('RABBITMQ_PORT')
    VHOST = os.getenv('RABBITMQ_VHOST')

    # Celery Configuration
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')
    RABBITMQ_URL = f"pyamqp://{USER}:{PASS}@{HOST}:{PORT}/{VHOST}"
    
    LOG_FILE = os.getenv('LOG_FILE')
    
    # SMTP Configurations
    SMTP_HOST = os.getenv('SMTP_HOST')
    SMTP_PORT = os.getenv('SMTP_PORT')
    SMTP_USER = os.getenv('SMTP_USER')
    SMTP_PASS = os.getenv('SMTP_PASS')
