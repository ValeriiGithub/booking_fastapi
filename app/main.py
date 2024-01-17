from __future__ import annotations

from datetime import date
from typing import Optional

import uvicorn
from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel

from app.bookings.router import router as router_bookings
from app.users.router import router as router_users

# TODO: Не реализованы в коде следующие роутеры
# from app.users.router import router_auth, router_users
from app.hotels.router import router as router_hotels

from app.pages.router import router as router_pages

app = FastAPI()

# app.include_router(router_auth)
app.include_router(router_users)
app.include_router(router_hotels)
app.include_router(router_bookings)

app.include_router(router_pages)


class HotelsSearchArgs:
    """
    Аргументы для get запросов
    """

    def __int__(
            self,
            location: str,
            date_from: date,
            date_to: date,
            has_spa: Optional[bool] = None,
            stars: Optional[int] = Query(None, ge=1, le=5),
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars


@app.get("/hotels")
def get_hotels(
        search_args: HotelsSearchArgs = Depends()
):
    return search_args


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
