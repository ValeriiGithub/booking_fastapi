from fastapi import APIRouter

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


@router.get("")
def get_bookings():
    pass


@router.get("/{bookings_id}")
def get_bookings_2(bookings_id):
    pass
