from fastapi import APIRouter, HTTPException

from app.users.auth import get_password_hash, verify_password
from app.users.dao import UsersDAO
from app.users.schemas import SUserRegister, SUserAuth

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"],
)


@router.post("/register")
async def register_user(user_data: SUserRegister):
    exiting_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if exiting_user:
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(user_data: SUserAuth):
    user = await UsersDAO.find_one_or_none(email=user_data.email)
    if not user:
        raise HTTPException(500)
    if user:
        password_is_valid = verify_password(user_data.password, user.password)
        if not password_is_valid:
            raise HTTPException(500)
