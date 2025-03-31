"""Инициализация БД"""
# pylint: disable = [import-error, no-name-in-module]

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from dodo.dodo.config import REAL_DATABASE_URL

async_engine = create_async_engine(
    REAL_DATABASE_URL,
    pool_size=20,
    max_overflow=10,
    pool_recycle=3600,
    pool_pre_ping=True,
    echo=False
)

async_session_factory = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    """Базовый класс декларативного подхода"""
    # pylint: disable = too-few-public-methods
    repr_cols_num = 3
    repr_cols = tuple()

    def __repr__(self):
        """Представления"""
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")

        return f"<{self.__class__.__name__} {', '.join(cols)}>"
