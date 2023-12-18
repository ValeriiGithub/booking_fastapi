from sqlalchemy import select

from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)  # SELECT * FROM bookings;
            result = await session.execute(query)  # исполни запрос query
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)  # SELECT * FROM bookings;
            result = await session.execute(query)  # исполни запрос query
            return result.scalars().all()
