import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(contact, template, target):
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = contact['Email']
    msg['Subject'] = template['subject']
    body = template['body'].replace("{{name}}", contact['Name'])
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP_SSL('smtp.titan.email', 465) as server:
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)