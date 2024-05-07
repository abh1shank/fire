from email.message import EmailMessage
import ssl
import smtplib
from config import sender_email,password,receiver_email
def send_alert(detection):
    subject = 'ALERT !!!'
    body = f'A {detection} HAS BEEN DETECTED !!'

    em = EmailMessage()
    em['From'] = sender_email
    em['To'] = receiver_email
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(sender_email, password)
        server.send_message(em)

