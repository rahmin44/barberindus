from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Product(BaseModel):
    id: str
    name: str
    category: str
    description: str
    price: float

products_db = [
    Product(id="p1", name="Пудра", category="Волосы", description="Пудра для укладки", price=1500),
    Product(id="p2", name="Воск", category="Волосы", description="Воск для волос", price=1000),
    Product(id="p3", name="Спрей", category="Волосы", description="Спрей для фиксации", price=999),
    Product(id="p4", name="Глина", category="Волосы", description="Глина для укладки", price=700),
    Product(id="p5", name="Бальзам", category="Для бороды", description="Увлажняющий бальзам", price=1200),
    Product(id="p6", name="Масло", category="Для бороды", description="Питательное масло", price=1300),
]

@app.get("/products", response_model=List[Product])
async def get_products():
    return products_db
