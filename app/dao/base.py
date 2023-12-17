from sqlalchemy import select

from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model)  # SELECT * FROM bookings;
            result = await session.execute(query)  # исполни запрос query
            return result.scalars().all()
