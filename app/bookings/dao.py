# работа с базой данных с использованием реализации паттерна data access object (DAO)

from app.bookings.models import Bookings
from app.dao.base import BaseDAO


class BookingDAO(BaseDAO):
    model = Bookings

    @classmethod
    async def add(cls):
        pass
