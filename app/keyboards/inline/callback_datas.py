from aiogram.utils.callback_data import CallbackData

subscribe_with_cargo = CallbackData("subscribe", "cargo_id")

cargo_data = CallbackData("show_cargo", "cargo_id")

show_page_data = CallbackData("show_cargos", "page")

show_page_ar = CallbackData("show_ar_types", "page")
artype_data = CallbackData("artype", "id")
show_page_load = CallbackData("show_load_types", "page")
loadtype_data = CallbackData("loadtypes", "id")