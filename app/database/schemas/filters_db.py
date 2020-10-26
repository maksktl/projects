from aiogram import types
from sqlalchemy import Column, BigInteger, String, sql, Boolean, DateTime

from database.db_gino import BaseModel


class ArType(BaseModel):
    __tablename__ = 'ar_type'
    query: sql.Select

    id = Column(BigInteger, primary_key=True)
    type = Column(String(100))


class LoadType(BaseModel):
    __tablename__ = 'loadtypes'
    query: sql.Select

    id = Column(BigInteger, primary_key=True)
    type = Column(String(100))
