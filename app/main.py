from fastapi import FastAPI


app = FastAPI()

@app.get("/hotels")
def get_hotels():
    return "Отель Бридж Резорт 5 звезд"
