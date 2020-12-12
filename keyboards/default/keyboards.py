from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ℹ️ Помощь")],
        [KeyboardButton(text="📨 Отправить письмо")],
    ],
    resize_keyboard=True
)

country_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇵🇱 Польша")],
        [KeyboardButton(text="🇺🇦 Украина")],
        [KeyboardButton(text="🇰🇿 Казахстан")],
        [KeyboardButton(text="🇺🇿 Узбекистан")],
        [KeyboardButton(text="🇧🇬 Болгария")],
        [KeyboardButton(text="🇷🇴 Румыния")],
        [KeyboardButton(text="🇵🇹 Португалия")],
        [KeyboardButton(text="◀️ Назад")],
    ],
    resize_keyboard=True
)

back_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="◀️ Назад")],
    ],
    resize_keyboard=True
)
