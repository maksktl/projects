from aiohttp import ClientSession

from config import TGBOT_TOKEN

URL = 'https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}'


async def send_message(chat_id: str, text: str):
    async with ClientSession() as session:
        async with session.post(URL.format(TGBOT_TOKEN, chat_id, text)) as response:
            pass
