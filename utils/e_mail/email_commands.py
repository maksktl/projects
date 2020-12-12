from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from data.config import E_LOGIN
from loader import email_sender

import re


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


def send_email(to_addr, subject, message):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = E_LOGIN
    msg['To'] = to_addr

    text = cleanhtml(message)
    part1 = MIMEText(text, "text-plain")
    part2 = MIMEText(message, "html")

    msg.attach(part1)
    msg.attach(part2)
    email_sender.sendmail(E_LOGIN, to_addr, msg.as_string())
