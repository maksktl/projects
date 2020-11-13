from aiogram import Dispatcher

from .call import CallAnswerMiddleware
from .throttling import ThrottlingMiddleware


def setup(dp: Dispatcher):
    # dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(CallAnswerMiddleware())
