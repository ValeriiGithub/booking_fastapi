from fastapi import APIRouter

from bookings.dao import BookingDAO

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


@router.get("")
async def get_bookings():
    return BookingDAO.find_all()
