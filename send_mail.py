import smtplib
from email.mime.text import MIMEText



def send_mail(Name,Phone_Number, Email, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = "529f5524d7ef67"
    password = "99d4490e9ee884"
    message = f"<h3> New Feedback Submission </h3><ul><li>Customer:{Name}</li><li>Email:{Email}</li><li>Rating:{rating}</li><li>Comments:{comments}</li></ul><h3>{Phone_Number}</h3>"

    sender_email = "email1@example.com"
    receiver_email = "email2@example.com"
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Form Feedback'
    msg['From'] = sender_email
    msg['to'] = receiver_email

    # send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
