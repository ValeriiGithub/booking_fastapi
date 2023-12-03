from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import settings

# Создаем синглтон подключения к БД по URL
engine = create_async_engine(settings.DATABASE_URL)

# Создаем генератор сессий (транзакции)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    """
    Данный класс используется для миграций
    Здесь будут аккумулироваться все данные о всех моделях/таблицах,
    чтобы затем alembic мог сравнить состояния для создания миграций
    """
    pass
