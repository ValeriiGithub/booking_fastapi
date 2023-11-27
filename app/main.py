import uvicorn
from fastapi import FastAPI
from  typing import Optional

app = FastAPI()

@app.get("/hotels")
def get_hotels(
        location,
        date_from,
        date_to,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = None,

):

    return date_from, date_to


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
