from pydantic import BaseModel


class Item(BaseModel):
    surname: str
    name: str
    lastname: str

    birth_date: str
    passport: dict
    vin: str