from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ℹ️ Помощь", callback_data="help")],
        [KeyboardButton(text="📨 Отправить письмо", callback_data="send")],
    ],
    resize_keyboard=True
)

country_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇵🇱 Польша", callback_data="country:Polish")],
        [KeyboardButton(text="🇺🇦 Украина", callback_data="country:Ukraine")],
        [KeyboardButton(text="🇰🇿 Казахстан", callback_data="country:Kazakhstan")],
        [KeyboardButton(text="🇺🇿 Узбекистан", callback_data="country:Uzbekistan")],
        [KeyboardButton(text="🇧🇬 Болгария", callback_data="country:Bulgaria")],
        [KeyboardButton(text="🇷🇴 Румыния", callback_data="country:Rumania")],
        [KeyboardButton(text="🇵🇹 Португалия", callback_data="country:Portugal")],
    ],
    resize_keyboard=True
)
