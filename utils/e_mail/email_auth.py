from data.config import E_LOGIN, E_PASSWORD


def on_shutdown():
    from loader import email_sender
    email_sender.close()


def on_startup():
    from loader import email_sender
    email_sender.starttls()
    email_sender.login(E_LOGIN, E_PASSWORD)
