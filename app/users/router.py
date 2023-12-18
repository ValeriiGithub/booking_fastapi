from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"],
)

@router.post("/register"):
async def register_user()
    