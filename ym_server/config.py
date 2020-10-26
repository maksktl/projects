import os

# SSL settings
SSL_DIR = os.getenv('SSL_DIR')
SSL_CERT = os.getenv('SSL_CERT')
SSL_PRIV = os.getenv('SSL_PRIV')

# Postgressql
PG_HOST = os.getenv('PG_HOST')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')

# Yandex-money
YM_HOST = os.getenv('YM_HOST')
YM_PORT = os.getenv('YM_PORT')
YM_WALLET_ID = os.getenv('YM_WALLET_ID')
SUBSCRIBE_PRICE1 = os.getenv('SUBSCRIBE_PRICE1')
SUBSCRIBE_PRICE3 = os.getenv('SUBSCRIBE_PRICE3')
SUBSCRIBE_PRICE6 = os.getenv('SUBSCRIBE_PRICE6')
NOTIFICATION_SECRET = os.getenv('NOTIFICATION_SECRET')

# Telegram token
TGBOT_TOKEN = os.getenv('TGBOT_TOKEN')
