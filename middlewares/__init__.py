from aiogram import Dispatcher

from .call import CallAnswerMiddleware


def setup(dp: Dispatcher):
    dp.middleware.setup(CallAnswerMiddleware())
