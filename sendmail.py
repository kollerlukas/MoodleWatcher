# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText
# Import mails from external file
from creds import FROM_ADDR
from creds import TO_ADDR
# import google app passwd from external file
from creds import APP_PASSWD

class MailHelper:

    def __init__(self):
        self.startServer()

    def startServer(self):
        # start gmail smtp server
        server = smtplib.SMTP('smtp.gmail.com', 587)  # port 465 or 587
        server.ehlo()
        server.starttls()
        server.ehlo()
        # login into Server
        server.login(FROM_ADDR, APP_PASSWD)
        self.server = server

    def sendMail(self, sbj, msg):
        # create message body
        msgbd = MIMEText(msg)
        msgbd['Subject'] = sbj
        msgbd['From'] = FROM_ADDR
        msgbd['To'] = TO_ADDR
        # send mail
        self.server.sendmail(FROM_ADDR, TO_ADDR, msgbd.as_string())

    def quit(self):
        # close server
        self.server.quit()
