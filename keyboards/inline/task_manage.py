from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📃 Название задачи")],
        [InlineKeyboardButton(text="📍 Местоположение")],
        [
            InlineKeyboardButton(text="📆 День"),
            InlineKeyboardButton(text="⌚️ Время"),
        ],
    ]
)

