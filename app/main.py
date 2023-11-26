import uvicorn
from fastapi import FastAPI


app = FastAPI()

@app.get("/hotels/{hotel_id}")
def get_hotels(hotel_id: int, date_from, date_to):
    # return "Отель Бридж Резорт 5 звезд"
    return hotel_id, date_from, date_to


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
