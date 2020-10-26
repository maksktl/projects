import logging
import ssl
import time

from aiogram import Dispatcher
from aiogram.utils.executor import start_webhook

from bot_loader import bot
from config import SSL_DIR, SSL_CERT, SSL_PRIV, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT, WEBHOOK_HOST, WEBHOOK_PORT, \
    TG_ADMINS_ID
from database import db_gino

WEBHOOK_URL = f'{WEBHOOK_HOST}:{WEBHOOK_PORT}{WEBHOOK_PATH}'


async def on_startup(dispatcher: Dispatcher):
    await db_gino.on_startup()

    # Check webhook
    webhook = await bot.get_webhook_info()

    # If URL is bad
    if webhook.url != WEBHOOK_URL:
        # If URL doesnt match current - remove webhook
        if not webhook.url:
            await bot.delete_webhook()

    # # Set new URL for webhook
    await bot.set_webhook(WEBHOOK_URL, certificate=open(f'{SSL_DIR}{SSL_CERT}', 'rb').read())

    # Send message to admin
    await bot.send_message(TG_ADMINS_ID[0], "Я запущен!")


async def on_shutdown(dispatcher: Dispatcher):
    # insert code here to run it before shutdown

    # Send message to admin
    await bot.send_message(TG_ADMINS_ID[0], "Я выключен!")

    # Close bot
    await bot.close()
    #
    # Close DB connection (if used)
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == '__main__':
    from handlers import dp

    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(f'{SSL_DIR}{SSL_CERT}', f'{SSL_DIR}{SSL_PRIV}')

    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
        ssl_context=context
    )
