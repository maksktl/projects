from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import artype_data, show_page_ar, show_page_load, loadtype_data


def artype_keyboard(items: list, prev_page: int, next_page: int):
    keyboard = InlineKeyboardMarkup()
    for item in items:
        keyboard.add(
            InlineKeyboardButton(
                text=item.type,
                callback_data=artype_data.new(id=item.id)
            )
        )
    navigation = [
        InlineKeyboardButton(text="⬅", callback_data=show_page_ar.new(page=prev_page)),
        InlineKeyboardButton(text="Назад к фильтрам", callback_data="cargos_back"),
        InlineKeyboardButton(text="➡️", callback_data=show_page_ar.new(page=next_page)),
    ]
    keyboard.add(*navigation)
    return keyboard


def loadtypes_keyboard(items: list, prev_page: int, next_page: int):
    keyboard = InlineKeyboardMarkup()
    for item in items:
        keyboard.add(
            InlineKeyboardButton(
                text=item.type,
                callback_data=loadtype_data.new(id=item.id)
            )
        )
    navigation = [
        InlineKeyboardButton(text="⬅", callback_data=show_page_load.new(page=prev_page)),
        InlineKeyboardButton(text="Назад к фильтрам", callback_data="cargos_back"),
        InlineKeyboardButton(text="➡️", callback_data=show_page_load.new(page=next_page)),
    ]
    keyboard.add(*navigation)
    return keyboard