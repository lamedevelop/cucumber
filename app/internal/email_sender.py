import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.internal.config_loader import ConfigLoader


class EmailSender:

    def __init__(self, email: str = None):
        config = ConfigLoader.getConfig()
        self.sender = config.MAIL_SENDER
        self.receiver = email
        self.password = config.MAIL_PASSWORD
        self.port = config.MAIL_PORT
        self.smtp_server = config.MAIL_SMTP_SERVER
        self.mail = MIMEMultipart()

    def send(self, message: dict):
        mail_content = f"This message was automatically sent from cucumber.\n" \
                       f"{message['content']}"
        self.mail['From'] = self.sender
        self.mail['Subject'] = message['subject']
        self.mail.attach(MIMEText(mail_content, 'plain'))
        self.mail['To'] = self.receiver

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(
                self.smtp_server,
                self.port,
                context=context
        ) as server:
            server.login(
                self.sender,
                self.password
            )

            server.sendmail(
                self.sender,
                self.receiver,
                self.mail.as_string()
            )
