from data.config import E_LOGIN
from loader import email_sender


def send_email(to_addr, subject, message):
    BODY = '\r\n'.join([
        f"From: {E_LOGIN}",
        f"To: {to_addr}",
        f"Subject: {subject}",
        "",
        message
    ])
    email_sender.sendmail(E_LOGIN, to_addr, BODY)
