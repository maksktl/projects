"""Аутентификация пользователей — проверяем есть ли пользователь с таким телеграмм ID в бд"""

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import MessageError

from database.schemas.user import User



class AccessMiddleware(BaseMiddleware):

    def __init__(self):
        super().__init__()

    async def on_pre_process_message(self, message: types.Message, data: dict, *arg, **kwargs):
        data['user'] = await User().get_or_create(message.from_user, get_parent_ref(message.text))

    async def on_pre_process_callback_query(self, callback_query: types.CallbackQuery, data: dict, *arg, **kwargs):
        data['user'] = await User().get_or_create(callback_query.from_user)


def get_parent_ref(message: str):
    try:
        message = message.split(' ')
    except AttributeError:
        return None

    if message[0] != "/start" or len(message) != 2:
        return None

    try:
        return int(message[-1])
    except ValueError:
        return None