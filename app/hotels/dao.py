# работа с базой данных с использованием реализации паттерна data access object (DAO)
from datetime import date

from sqlalchemy import and_, func, or_, select

from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.database import async_session_maker, engine
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms


# from app.logger import logger


class HotelDAO(BaseDAO):
    model = Hotels

    @classmethod
    async def find_all(cls, location: str, date_from: date, date_to: date):
        """
        WITH booked_rooms AS (
            SELECT room_id, COUNT(room_id) AS rooms_booked
            FROM bookings
            WHERE
                (date_from >= '2023-05-15' AND date_from <= '2023-06-20') OR
                (date_from <= '2023-05-15' AND date_to > '2023-05-15')
            GROUP BY room_id
        ),
        booked_hotels AS (
            SELECT hotel_id, SUM(rooms.quantity - COALESCE(rooms_booked, 0)) AS rooms_left
            FROM rooms
            LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
            GROUP BY hotel_id
        )
        SELECT * FROM hotels
        LEFT JOIN booked_hotels ON booked_hotels.hotel_id = hotels.id
        WHERE rooms_left > 0 AND location LIKE '%Алтай%';

        Этот запрос использует оператор WITH для определения двух общих табличных выражений (CTE): booked_rooms и booked_hotels. CTE - это временная таблица, которая существует только в рамках одного запроса. Они могут упростить и ускорить выполнение сложных запросов1.

        Первый CTE, booked_rooms, выбирает идентификаторы номеров и количество забронированных номеров из таблицы bookings, где дата заезда или выезда попадает в период с 15 мая по 20 июня 2023 года. Затем он группирует результаты по идентификаторам номеров.

        Второй CTE, booked_hotels, выбирает идентификаторы отелей и количество свободных номеров из таблицы rooms, используя левое объединение с CTE booked_rooms по идентификаторам номеров. Он вычитает количество забронированных номеров из общего количества номеров в каждом отеле и использует функцию COALESCE для замены NULL на 0. Затем он группирует результаты по идентификаторам отелей.

        После определения CTE основной запрос выбирает все столбцы из таблицы hotels, используя левое объединение с CTE booked_hotels по идентификаторам отелей. Он фильтрует результаты, оставляя только те отели, где количество свободных номеров больше 0 и местоположение содержит подстроку ‘Алтай’. Это означает, что запрос возвращает информацию об отелях, которые имеют доступные номера в Алтае в указанный период.
        """
        booked_rooms = (
            select(Bookings.room_id, func.count(Bookings.room_id).label("rooms_booked"))
            .select_from(Bookings)
            .where(
                or_(
                    and_(
                        Bookings.date_from >= date_from,
                        Bookings.date_from <= date_to,
                    ),
                    and_(
                        Bookings.date_from <= date_from,
                        Bookings.date_from > date_from,
                    )
                )
            )
            .group_by(Bookings.room_id)
            .cte("booked_rooms")
        )

        booked_hotels = (
            select(Rooms.hotel_id, func.sum(
                Rooms.quantity - func.coalesce(booked_rooms.c.rooms_booked, 0)
            ).label("rooms_left"))
            .select_from(Rooms)
            .join(booked_rooms, booked_rooms.c.room_id == Rooms.id, isouter=True)
            .group_by(Rooms.hotel_id)
            .cte("booked_hotels")
        )

        get_hotels_with_rooms = (
            # Код ниже можно было бы расписать так:
            # select(
            #     Hotels
            #     booked_hotels.c.rooms_left,
            # )
            # Но используется конструкция Hotels.__table__.columns. Почему? Таким образом алхимия отдает
            # все столбцы по одному, как отдельный атрибут. Если передать всю модель Hotels и
            # один дополнительный столбец rooms_left, то будет проблематично для Pydantic распарсить
            # такую структуру данных. То есть проблема кроется именно в парсинге ответа алхимии
            # Пайдентиком.
            select(
                Hotels.__table__.columns,
                booked_hotels.c.rooms_left,
            )
            .join(booked_hotels, booked_hotels.c.hotel_id == Hotels.id, isouter=True)
            .where(
                and_(
                    booked_hotels.c.rooms_legt > 0,
                    Hotels.location.like(f"%{location}%"),
                )
            )
        )

        async with async_session_maker() as session:
            # logger.debug(get_hotels_with_rooms.compile(engine, compile_kwargs={"literal_binds": True}))
            hotels_with_rooms = await session.execute(get_hotels_with_rooms)
            return hotels_with_rooms.mappings().all()
