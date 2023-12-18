from fastapi import APIRouter

from app.users.schemas import SUserRegister

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"],
)

@router.post("/register")
async def register_user(user_data: SUserRegister):
    exiting_user = 