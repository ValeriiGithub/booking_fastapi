from __future__ import annotations


from fastapi import FastAPI

from app.bookings.router import router as router_bookings

# TODO: Не реализованы в коде следующие роутеры
# from app.users.router import router_auth
from app.users.router import router as router_users
from app.hotels.router import router as router_hotels

from app.pages.router import router as router_pages

app = FastAPI()

# app.include_router(router_auth)
app.include_router(router_users)
app.include_router(router_hotels)
app.include_router(router_bookings)

app.include_router(router_pages)



