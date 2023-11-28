import uvicorn
from fastapi import FastAPI, Query
from  typing import Optional
from datetime import date

app = FastAPI()

@app.get("/hotels")
def get_hotels(
        location: str,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = Query(None, ge=1, le=5),
):
    return date_from, date_to


@app.post("/bookings")
def add_booking():
    pass

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
