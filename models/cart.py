from fastapi import FastAPI
from pydantic import BaseModel
import enum
import datetime
from typing import List

import DateTime

from domains.cart import CartId, Quantity
from domains.client import ClientId
from domains.product import Product, ProductId

#Default user friendly name "Cart #id" for example



class Cart(BaseModel):
    id: CartId
    clientId: ClientId
    userFriendlyName: str | None = "Mon Panier Aujourd'hui"
    create_at: datetime.datetime | None = datetime.datetime.now()
    updated_at: datetime.datetime | None = datetime.datetime.now()
    items: list[dict[ProductId, Quantity]] | None = []
