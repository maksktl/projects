from database.schemas.processfile import ProcessFile


async def get_photo_list(user_id: int) -> list:
    result = await ProcessFile.query.where(ProcessFile.user_id == user_id).gino.all()

    if result is None:
        return []
    return result
