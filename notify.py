from email.message import EmailMessage
import ssl
import smtplib

def send_alert(detection):
    sender_email = 'abhishanks.ic.21@nitj.ac.in'
    password = 'tnql boxq zlcv phge'
    receiver_email = 'saranabhishank13@gmail.com'
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

