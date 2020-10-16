from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.Photos import Photo
from utils.db_api.schemas.Voices import Voice
from utils.db_api.schemas.Users import User


async def add_photo(file_id: str, username: str, user_id: int):
    try:
        photo = Photo(file_id=file_id, username=username, user_id=int(user_id))
        await photo.create()

    except UniqueViolationError:
        pass


async def add_voice(file_id: str, username: str, user_id: int):
    try:
        voice = Voice(file_id=file_id, username=username, user_id=int(user_id))
        await voice.create()

    except UniqueViolationError:
        pass


async def add_user(user_id: str, username: str, total_photos: int = 0, total_voices: int = 0):
    try:
        user = User(user_id=str(user_id), username=username, total_photos=total_photos, total_voices=total_voices)
        await user.create()
    except UniqueViolationError:
        pass


async def add_photo_to_user(user_id: str):
    user = await get_user_by_id(str(user_id))
    await user.update(total_photos=(user.total_photos + 1)).apply()


async def add_voice_to_user(user_id: str):
    user = await get_user_by_id(str(user_id))
    await user.update(total_voices=(user.total_voices + 1)).apply()


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


async def load_users():
    item_list1 = await Photo.query.gino.all()
    item_list2 = await Voice.query.gino.all()

    for item in item_list1:
        user = await get_user_by_id(str(item.user_id))
        if user is None:
            await add_user(str(item.user_id), item.username, 1, 0)
        else:
            await add_photo_to_user(str(item.user_id))

    for item in item_list2:
        user = await get_user_by_id(str(item.user_id))
        if user is None:
            await add_user(str(item.user_id), item.username, 0, 1)
        else:
            await add_voice_to_user(str(item.user_id))


async def get_user_by_id(user_id: str):
    return await User.query.where(User.user_id == user_id).gino.first()


async def get_user_by_username(username: str):
    return await User.query.where(User.username == username).gino.first()


async def get_all_users():
    return await User.query.gino.all()


async def get_all_photos():
    return await Photo.query.gino.all()


async def get_all_voices():
    return await Voice.query.gino.all()
