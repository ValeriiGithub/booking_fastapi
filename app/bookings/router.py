from fastapi import APIRouter

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


@router.get("")
def get_bookings():
    pass



