from flask import Blueprint, request, jsonify, current_app
from .tasks import send_email
from datetime import datetime
from .config import Config
from datetime import datetime
import pytz

main = Blueprint('main', __name__)

"""
this route takes either two parameters:
 - sendmail : send an email to a recipient
 - talktome : logs the current time progress for an email in queue
"""
@main.route('/')
def handle_request():
    if 'sendmail' in request.args:
        recipient = request.args.get('sendmail')
        send_email.delay(recipient)
        return jsonify({"message": f"Email queued for sending to {recipient}"})
    elif 'talktome' in request.args:
        # Get the current time in Nigeria (WAT)
        nigeria_tz = pytz.timezone('Africa/Lagos')
        current_time = datetime.now(nigeria_tz).strftime("%Y-%m-%d %H:%M:%S %Z")
        # current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(Config.LOG_FILE, 'a') as log_file:
            log_file.write(current_time + "\n")
        return jsonify({"message": f"Current Time Logged:{current_time}"})
    else:
        return jsonify({"message": "Invalid request"})


"""
this route /logs:
 - it fetches the logs logged from the `/talktome` endpoint
"""
@main.route('/logs')
def show_logs():
    try:
        with open(Config.LOG_FILE, 'r') as log_file:
            logs = ''.join(log_file.readlines())
        return logs, 200, {'Content-Type': 'text/plain'}
    except FileNotFoundError:
        return "Log file not found", 404
    except PermissionError:
        return "Permission denied to access log file", 403
