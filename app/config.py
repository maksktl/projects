import os

# app settings
DOMAIN_NAME_OR_IP = os.getenv('DOMAIN_NAME_OR_IP')

# Work dir
WORKS_DIR = os.getenv('WORKS_DIR')

# SSL settings
SSL_DIR = os.getenv('SSL_DIR')
SSL_CERT = os.getenv('SSL_CERT')
SSL_PRIV = os.getenv('SSL_PRIV')

# Telegram token
TGBOT_TOKEN = os.getenv('TGBOT_TOKEN')

# Telegram admins ID
TG_ADMINS_ID = [int(ID) for ID in os.getenv('TG_ADMINS_ID').split(':')]

# Telegram webhook
WEBHOOK_HOST = os.getenv('WEBHOOK_HOST')
WEBHOOK_PORT = os.getenv('WEBHOOK_PORT')
WEBHOOK_PATH = os.getenv('WEBHOOK_PATH')

# Webhost
WEBAPP_HOST = os.getenv('WEBAPP_HOST')
WEBAPP_PORT = os.getenv('WEBAPP_PORT')

# Postgressql
PG_HOST = os.getenv('PG_HOST')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')

# Yandex-money
YM_HOST = os.getenv('YM_HOST')
YM_PORT = os.getenv('YM_PORT')
YM_WALLET_ID = os.getenv('YM_WALLET_ID')
SUBSCRIBE_PRICE = os.getenv('SUBSCRIBE_PRICE')
