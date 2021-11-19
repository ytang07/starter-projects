import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

from email_config import gmail_pass, user, host, port

# who are we sending this email to?
to = "internshipsdiscord@gmail.com"

# what is our subject line?
subject = "An example email"

# what is the body of the email?
body = "Hi,\nThis email is an example of how to send emails in Python\nBest, Yujian Tang"

def send_email(to, subject, body):
    # create message object
    message = MIMEMultipart()

    # add in header
    message['From'] = Header(user)
    message['To'] = Header(to)
    message['Subject'] = Header(subject)

    # attach message body as MIMEText
    message.attach(MIMEText(body, 'plain', 'utf-8'))
    
    # setup email server
    server = smtplib.SMTP_SSL(host, port)
    server.login(user, gmail_pass)

    # send email and quit server
    server.sendmail(user, to, message.as_string())
    server.quit()
