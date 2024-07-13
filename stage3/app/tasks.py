from celery import Celery
from email.mime.text import MIMEText
import smtplib
from flask import jsonify
from .config import Config

# 
celery = Celery('tasks', broker=Config.RABBITMQ_URL)

"""
sendmail function with rabitmq that is abstacted by the celery worker above
"""
@celery.task
def send_email(recipient):
    message = MIMEText("This is a test email from the messaging system.")
    message['Subject'] = "Test Email From Hendrixx"
    message['From'] = Config.SMTP_USERNAME
    message['To'] = recipient

    try:
        with smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT) as server:
            print(f"Connecting to {Config.SMTP_SERVER}:{Config.SMTP_PORT}")
            server.ehlo()
            print("Starting TLS")
            server.starttls()
            print(f"Logging in as {Config.SMTP_USERNAME}")
            server.login(Config.SMTP_USERNAME, Config.SMTP_PASSWORD)
            print(f"Sending email to {recipient}")
            server.sendmail(Config.SMTP_USERNAME, recipient, message.as_string())
            #server.send_message(message)
        return jsonify({"message: email sent successfully to {recipient}"})
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False