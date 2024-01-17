# работа с базой данных с использованием реализации паттерна data access object (DAO)
from datetime import date
from sqlalchemy import delete, insert, select, func, and_, or_
# from app.bookings.schemas import SBookingInfo
from app.dao.base import BaseDAO
from app.database import async_session_maker, engine

from app.bookings.models import Bookings
from app.hotels.models import Hotels


class HotelDAO(BaseDAO):
    model = Hotels

    @classmethod
    async def find_all(cls):
        pass
