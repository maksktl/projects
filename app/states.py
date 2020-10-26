from aiogram.dispatcher.filters.state import State, StatesGroup


class FilterSettings(StatesGroup):
    from_city = State()
    radius_from = State()
    to_city = State()
    radius_to = State()
    from_date = State()
    to_date = State()
    cargo_type = State()
    truck_type = State()
    weight = State()
    volume = State()

