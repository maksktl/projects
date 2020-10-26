import os

# app settings
DOMAIN_NAME_OR_IP = os.getenv('DOMAIN_NAME_OR_IP')

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

# Cargolink API
API_BASE_URL = os.getenv('API_BASE_URL')
API_CONSUMER_KEY=os.getenv('API_CONSUMER_KEY')
API_CONSUMER_SECRET_KEY=os.getenv('API_CONSUMER_SECRET_KEY')
API_TOKEN = os.getenv('API_TOKEN')
API_SECRET_TOKEN = os.getenv('API_SECRET_TOKEN')

# Yandex-money
YM_PORT = os.getenv('YM_PORT')
YM_WALLET_ID = os.getenv('YM_WALLET_ID')
SUBSCRIBE_PRICE1 = os.getenv('SUBSCRIBE_PRICE1')
SUBSCRIBE_PRICE3 = os.getenv('SUBSCRIBE_PRICE3')
SUBSCRIBE_PRICE6 = os.getenv('SUBSCRIBE_PRICE6')
