from __future__ import annotations

import uvicorn
from fastapi import FastAPI, Query, Depends
from typing import Optional, List
from datetime import date
from pydantic import BaseModel

app = FastAPI()


# class SHotel(BaseModel):
#     address: str
#     name: str
#     stars: int


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


class SBooking(BaseModel):
    """
    Валидация данных
    Поля, которые пользователь передает в post запросе
    СХЕМЫ для POST запросов
    """
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")
def add_booking(booking: SBooking):
    pass

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
