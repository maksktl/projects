from asyncpg import UniqueViolationError

from database.db_gino import db
from database.schemas.filters_db import ArType, LoadType
from functions import replace_number


async def select_all_artypes():
    return await ArType.query.gino.all()


async def select_all_loadtypes():
    return await LoadType.query.gino.all()


async def create_artype(id: int, type: str):
    try:
        artype = ArType(id=id, type=type)
        await artype.create()

    except UniqueViolationError:
        pass


async def create_loadtype(id: int, type: str):
    try:
        loadtype = LoadType(id=id, type=type)
        await loadtype.create()

    except UniqueViolationError:
        pass


async def get_load_by_id(id: int):
    return await LoadType.get(id)


async def get_artype_by_id(id: int):
    return await ArType.get(id)
