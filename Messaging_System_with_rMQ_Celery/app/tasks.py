from celery import Celery
from email.mime.text import MIMEText
import smtplib
from flask import jsonify, current_app
from .config import Config 

"""
    Creates and configure a Celery instance for the Flask app.

    Args:
        app (Flask): The Flask application instance

    Returns:
        Celery: Configured Celery instance
"""
def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['RABBITMQ_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

celery = Celery()

"""
sendmail function with rabitmq that is abstacted by the celery worker above
"""
@celery.task
def send_email(recipient):
    config = current_app.config
    message = MIMEText("This is a test email from the messaging system.")
    message['Subject'] = "Test Email From Hendrixx"
    message['From'] = Config.SMTP_USER
    message['To'] = recipient

    try:
        with smtplib.SMTP(Config.SMTP_HOST, Config.SMTP_PORT, timeout=30) as server:
            # server.connect(Config.SMTP_HOST, Config.SMTP_PORT)
            print(f"Connecting to {Config.SMTP_HOST}")
            server.ehlo()
            print("Starting TLS")
            server.starttls()
            server.ehlo()
            print(f"Logging in as {Config.SMTP_USER}")
            server.login(Config.SMTP_USER, Config.SMTP_PASS)
            print(f"Sending email to {recipient}")
            server.sendmail(Config.SMTP_USER, recipient, message.as_string())
            #server.send_message(message)
        return f"email sent successfully to {recipient}"
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False
