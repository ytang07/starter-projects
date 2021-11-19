from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
import smtplib
import os

from email_config import gmail_pass, user, host, port

# who are we sending this email to?
to = "internshipdiscord@gmail.com"

# what is our subject line?
subject = "An example email"

# what is the body of the email?
body = "Hi,\nThis email is an example of how to send emails in Python\nBest, Yujian Tang"

# what is the name of the file we want to attach?
filename = "beginner\\email\\attachment.txt"

def send_email_w_attachment(to, subject, body, filename):
    # create message object
    message = MIMEMultipart()

    # add in header
    message['From'] = Header(user)
    message['To'] = Header(to)
    message['Subject'] = Header(subject)

    # attach message body as MIMEText
    message.attach(MIMEText(body, 'plain', 'utf-8'))

    # locate and attach desired attachments
    att_name = os.path.basename(filename)
    _f = open(filename, 'rb')
    att = MIMEApplication(_f.read(), _subtype="txt")
    _f.close()
    att.add_header('Content-Disposition', 'attachment', filename=att_name)
    message.attach(att)

    # setup email server
    server = smtplib.SMTP_SSL(host, port)
    server.login(user, gmail_pass)

    # send email and quit server
    server.sendmail(user, to, message.as_string())
    server.quit()

send_email_w_attachment(to, subject, body, filename)