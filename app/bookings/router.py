from __future__ import annotations
from typing import List

from fastapi import APIRouter

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


@router.get("")
async def get_bookings() -> List[SBooking]:
    return await BookingDAO.find_all()
