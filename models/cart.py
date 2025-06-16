from fastapi import FastAPI
from pydantic import BaseModel
import enum
import datetime
from typing import List

import DateTime

from domains.client import ClientId
from domains.product import Product, ProductId

#Default user friendly name "Cart #id" for example

type CartId = int
type Quantity = int

class Cart(BaseModel):
    id: CartId
    clientId: ClientId
    userFriendlyName: str | None
    create_at: datetime.datetime | None
    updated_at: datetime.datetime | None
    items: list[tuple[ProductId, Quantity]] | None
