import logging
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Cargo:
    id: str
    from_city: str
    to_city: str
    from_date: str
    to_date: str
    short_info: str
    info: str
    price: str
    contact: str
    type: str = ""
    volume: float = 0


def get_cargos(**kwargs):
    from load_all import cargo_api
    cargos = cargo_api.search_offers_cargo(**kwargs)
    # logging.debug(cargos)
    cargos = cargos.get('data')

    if cargos is None:
        return None

    result = []
    for cargo in cargos:
        result.append(Cargo(
            id=cargo.get('id'),
            from_city=cargo.get('city_name_from'),
            to_city=cargo.get('city_name_to'),
            from_date=datetime.utcfromtimestamp(cargo.get('from_datetime')).strftime('%d-%m-%Y'),
            to_date=datetime.utcfromtimestamp(cargo.get('to_datetime')).strftime('%d-%m-%Y'),
            contact=str(f"{cargo.get('gp_phone')}\n"
                        f"Фирма: {cargo.get('gp_firmname')}\n"
                        f"ФИО: {cargo.get('gp_fio')}\n"
                        f"Skype: {cargo.get('gp_skype')}\n"
                        f"E-mail: {cargo.get('gp_email')}"),
            price=str(f'{cargo.get("cargo_rate_price")} RUB'),
            short_info=str(f'{cargo.get("offers_cargo_name")} {float(cargo.get("weight"))} т, '),
            info=str(f"{cargo.get('offers_cargo_name')} {float(cargo.get('weight'))} т,\n"
                     f"{cargo.get('v_qube')} куб. метра, {cargo.get('description')}\n"
                     f"Тип кузова: {cargo.get('car_type_name')}\n"
                     f""),
            volume=float(cargo.get('v_qube')),
            type=cargo.get('offers_cargo_name')
        ))
    return result


def get_cargo_by_id(id: str):
    from load_all import cargo_api
    cargo = cargo_api.offer_cargo(int(id))
    # logging.debug(cargo)
    cargo = Cargo(
        id=cargo.get('offers_id'),
        from_city=cargo.get('city_name_from'),
        to_city=cargo.get('city_name_to'),
        from_date=datetime.utcfromtimestamp(int(float(cargo.get('from_date_timestamp')))).strftime('%d-%m-%Y'),
        to_date=datetime.utcfromtimestamp(int(float(cargo.get('to_date_timestamp')))).strftime('%d-%m-%Y'),
        contact=str(f"{cargo.get('gp_phone')}\n"
                    f"Фирма: {cargo.get('gp_firmname')}\n"
                    f"ФИО: {cargo.get('gp_fio')}\n"
                    f"Skype: {cargo.get('gp_skype')}\n"
                    f"E-mail: {cargo.get('gp_email')}"),
        price=str(f'{cargo.get("cargo_rate_price")} {cargo.get("cargo_rate_currency")}'),
        short_info=str(f'{cargo.get("offers_cargo_name")} {float(cargo.get("weight"))} т, '),
        info=str(f"{cargo.get('offers_cargo_name')} {float(cargo.get('weight'))} т,\n"
                 f"{cargo.get('v_qube')} куб. метра, {cargo.get('description')}\n"
                 f"Тип кузова: {cargo.get('car_type_name')}\n"
                 f"")
    )
    return cargo
