async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    from utils.e_mail import email_auth
    email_auth.on_startup()


async def on_shutdown(dp):
    from utils.e_mail import email_auth
    email_auth.on_shutdown()

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
