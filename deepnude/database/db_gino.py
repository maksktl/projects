from gino import Gino
from gino.schema import GinoSchemaVisitor

from config import POSTGRES_USER, POSTGRES_PASSWORD, PG_HOST, POSTGRES_DB

db = Gino()


# Пример из https://github.com/aiogram/bot/blob/master/app/models/db.py
async def on_startup():
    await db.set_bind(f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{PG_HOST}/{POSTGRES_DB}')

    # Create tables
    db.gino: GinoSchemaVisitor
    await db.gino.create_all()

