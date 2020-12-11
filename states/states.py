from aiogram.dispatcher.filters.state import StatesGroup, State


class State(StatesGroup):
    country = State()
    product_name = State()
    link = State()
    email = State()