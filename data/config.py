import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

admins = [
    os.getenv("ADMIN_ID"),
]

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}

#Email zone
E_LOGIN = str(os.getenv("E_LOGIN"))
E_PASSWORD = str(os.getenv("E_PASSWORD"))
SMTP_SERVER = str(os.getenv("SMTP_SERVER"))
SMTP_PORT = int(os.getenv("SMTP_PORT"))
