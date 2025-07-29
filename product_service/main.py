from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
products = {}

class Product(BaseModel):
    id: int
    name: str
    price: float

@app.post("/add")
def add_product(p: Product):
    if p.id in products:
        raise HTTPException(400, "Product exists")
    products[p.id] = p
    return {"message": "Added"}

@app.get("/list")
def list_products():
    return list(products.values())

@app.get("/get/{id}")
def get_product(id: int):
    if id not in products:
        raise HTTPException(404, "Not found")
    return products[id]
