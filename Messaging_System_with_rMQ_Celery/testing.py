import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'lengedandungjoshua@gmail.com'
SMTP_PASSWORD = 'bdqc onad rqed ynpq'

message = MIMEText("This is a test email from the messaging system.")
message['Subject'] = "Test Email From Hendrixx"
message['From'] = SMTP_USERNAME
message['To'] = 'devhendrixx@gmail.com'

try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, 'devhendrixx@gmail.com', message.as_string())
    print("Email sent successfully")
except Exception as e:
    print(f"Error sending email: {str(e)}")
