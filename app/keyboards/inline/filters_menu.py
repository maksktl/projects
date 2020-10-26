from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_datas import show_page_data, show_page_ar, show_page_load


def filter_menu(from_city: str = "Откуда", to_city: str = "Куда", from_date: str = "С даты",
                to_date: str = "До даты", artype: str = "Тип кузова", loadtype: str = "Тип выгрузки",
                weight_max: str = "Вес", v_qube_max: str = "Объем", radius_from: str = "радиус",
                radius_to: str = "радиус", **kwargs):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=str(f'🔼 {from_city}'), callback_data="from_city"),
                InlineKeyboardButton(text=str(f'🔘 {radius_from}'), callback_data='radius_from')
            ],
            [
                InlineKeyboardButton(text=str(f'🔽 {to_city}'), callback_data="to_city"),
                InlineKeyboardButton(text=str(f'🔘 {radius_to}'), callback_data='radius_to')
            ],
            [
                InlineKeyboardButton(text=str(f'🗓 {from_date}'), callback_data="from_date"),
                InlineKeyboardButton(text=str(f'🗓 {to_date}'), callback_data="to_date")
            ],
            [
                InlineKeyboardButton(text=str(f'🚚 {artype}'), callback_data=show_page_ar.new(page=1))
            ],
            [
                InlineKeyboardButton(text=str(f'📤 {loadtype}'), callback_data=show_page_load.new(page=1))
            ],
            [
                InlineKeyboardButton(text=str(f'⚖️{weight_max}'), callback_data="weight"),
                InlineKeyboardButton(text=str(f'🔵 {v_qube_max}'), callback_data="volume")
            ],
            [
                InlineKeyboardButton(text="🚫 Отмена", callback_data="cancel")

            ],
            [
                InlineKeyboardButton(text="🔍 Поиcк", callback_data=show_page_data.new(page=1))
            ]
        ]
    )


cancel_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Назад к фильтрам", callback_data="cargos_back")]
    ]
)
