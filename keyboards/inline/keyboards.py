from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Тип техники
tech_type = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Бульдозеры", callback_data="bulldozers")],
        [InlineKeyboardButton(text="Эксковаторы", callback_data="excavator")],
    ]
)

# Номер техники Бульдозер
bulldozer_num = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Б1111", callback_data="bull:Б1111")],
        [InlineKeyboardButton(text="Б2222", callback_data="bull:Б2222")],
        [InlineKeyboardButton(text="Б3333", callback_data="bull:Б3333")],
        [InlineKeyboardButton(text="◀️Назад", callback_data="start")],
    ]
)

# Номер техники Эксковатор
excavator_num = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Э1111", callback_data="exc:Э1111")],
        [InlineKeyboardButton(text="Э2222", callback_data="exc:Э2222")],
        [InlineKeyboardButton(text="Э3333", callback_data="exc:Э3333")],
            [InlineKeyboardButton(text="◀️Назад", callback_data="start")],
    ]
)

# Список ремонта Бульдозера
bull_remont_list = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Замена тормозной системы", callback_data="bull_remont:1")],
        [InlineKeyboardButton(text="Замена цепей", callback_data="bull_remont:2")],
        [InlineKeyboardButton(text="◀️Назад", callback_data="bulldozers")],

    ]
)

# Список ремонта Эксковатора
exc_remont_list = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Замена масла", callback_data="exc_remont:1")],
        [InlineKeyboardButton(text="Замена детали", callback_data="exc_remont:2")],
        [InlineKeyboardButton(text="◀️Назад", callback_data="excavator")],

    ]
)
