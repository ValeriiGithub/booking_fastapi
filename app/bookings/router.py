from fastapi import APIRouter
from sqlalchemy import select

from app.bookings.models import Bookings
from app.database import async_session_maker

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


@router.get("")
async def get_bookings():
    with async_session_maker() as session:
        query = select(Bookings)  # SELECT * FROM bookings;
        result = await session.execute(query)  # исполни запрос query
        return result.scalars().all()

