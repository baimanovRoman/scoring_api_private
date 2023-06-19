from fastapi import FastAPI, Depends, Request
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from services.get_data import GetData
from model.base_model import Item
import uvicorn



origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://127.0.0.1",
    "http://profile.test"
]


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def get_body(request: Request):
    return await request.body()


@app.post("/")
async def read_root(item: Item):
    get_data = GetData(item)
    result = get_data()
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
