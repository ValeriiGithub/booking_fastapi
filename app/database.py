from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from settings import DATABASE_URL


# Создаем URL БД
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# asyncpg - асинхронная работа
# psycopg2 - синхронная работа

# Создаем синглтон подключения к БД по URL
engine = create_async_engine(DATABASE_URL)

# Создаем генератор сессий (транзакции)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    """
    Данный класс используется для миграций
    Здесь будут аккумулироваться все данные о всех моделях/таблицах,
    чтобы затем alembic мог сравнить состояния для создания миграций
    """
    pass
