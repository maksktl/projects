from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.Photos import Photo
from utils.db_api.schemas.Voices import Voice


async def add_photo(file_id: str, username: str, user_id: int):
    try:
        photo = Photo(file_id=file_id, username=username, user_id=user_id)
        await photo.create()

    except UniqueViolationError:
        pass


async def add_voice(file_id: str, username: str, user_id: int):
    try:
        voice = Voice(file_id=file_id, username=username, user_id=user_id)
        await voice.create()

    except UniqueViolationError:
        pass


async def get_photo(id: int):
    photo = await Photo.get(id)
    return photo


async def get_voice(id: int):
    voice = await Voice.get(id)
    return voice


async def photos_count():
    total = await db.func.count(Photo.id).gino.scalar()
    return total


async def voices_count():
    total = await db.func.count(Voice.id).gino.scalar()
    return total
