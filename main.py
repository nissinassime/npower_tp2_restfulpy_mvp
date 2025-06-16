from fastapi import FastAPI
from pydantic import BaseModel

from data.cartsdao import CartsDao
from data.clientsdao import ClientsDao
from data.productsdao import ProductsDao

cartsDbInMemory = CartsDao()
cartsDbInMemory.load_from_json('data/carts.json')
print(cartsDbInMemory.db)

# clientsDbInMemory = ClientsDao()
# clientsDbInMemory.load_from_csv("data/clients.csv.txt")
# print(clientsDbInMemory.db)
#
# productsDbInMemory = ProductsDao()
# productsDbInMemory.load_from_csv("data/produits.csv.txt")
# print(productsDbInMemory.db)




class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item


# @app.get("/carts/")
# async def get_carts():
#


# @app.get("/clients/")
# async def get_clients():
#     return clientsDbInMemory.db

# @app.get("/client/{id}")
# async def get_client(id: int):


# @app.get("/orders/")
# async def get_orders():
#     return clientsDBInMemory.db


# # NOTE TP2 1. Liste de produits disponibles
# #  Produit = tuple (id, nom, prix)
# @app.get("/products/")
# async def get_products():
#     return productsDbInMemory.db








# from typing import Union
#
# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/")
# def read_root():
#     return {"Hello": "FastAPI World"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}



# from fastapi import FastAPI
# import uvicorn
#
# app = FastAPI()
#
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8765, reload=True)