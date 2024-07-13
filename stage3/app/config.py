import os
from dotenv import load_dotenv

load_dotenv()

"""
Credentials configurations for  rabitmq and smtp
"""
class Config:
    USER = os.getenv('RABBITMQ_USER')
    PASS = os.getenv('RABBITMQ_PASS')
    HOST = os.getenv('RABBITMQ_HOST')
    PORT = os.getenv('RABBITMQ_PORT')
    VHOST = os.getenv('RABBITMQ_VHOST')


    RABBITMQ_URL = f"pyamqp://{USER}:{PASS}@{HOST}:{PORT}/{VHOST}"

    LOG_FILE = os.getenv('LOG_FILE')

    SMTP_SERVER = os.getenv('SMTP_SERVER',)
    SMTP_PORT = os.getenv('SMTP_PORT')
    SMTP_USERNAME = os.getenv('SMTP_USER')
    SMTP_PASSWORD = os.getenv('SMTP_PASS')
    # SMTP_RECIPIENT= os.getenv()
