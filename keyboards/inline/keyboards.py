from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

tech_type = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Бульдозеры", callback_data="bulldozers")],
        [InlineKeyboardButton(text="Эксковаторы", callback_data="excavator")]
    ]
)