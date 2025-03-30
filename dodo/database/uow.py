"""Юнит для работы с БД"""
from typing import Union

from sqlalchemy import text
from sqlalchemy.exc import DBAPIError, IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from dodo.database import async_session_factory
from dodo.database.models import DodoProductModel
from dodo.dodo.logger import LOGER

OrmObj = Union[
    DodoProductModel,
]

class UoW:
    """Юнит для работы с БД"""

    def __init__(self):
        self._factory: AsyncSession = async_session_factory()

    @LOGER.catch
    async def create_obj(self, obj: OrmObj, **kwargs) -> OrmObj.id | None:
        """метод для создания обьекта"""
        async with self._factory as session:
            stmt = obj(**kwargs)
            session.add(stmt)
            try:
                res = stmt.id
                await session.commit()
                return res
            except (IntegrityError, DBAPIError) as e:
                LOGER.warning(e)
                await session.close()
        return None

    @LOGER.catch
    async def test_connect(self) -> bool | ConnectionRefusedError:
        """тест соединения"""
        async with self._factory as session:
            try:
                query = text("SELECT 1")
                await session.execute(query)
                return True
            except ConnectionRefusedError as e:
                return e
