import datetime
from enum import Enum
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import datetime
import enum

from domains.cart import CartId
from domains.client import ClientId
from domains.order import Status, OrderId
from domains.product import Product, ProductId
from utils.generate_ids import generate_ids

#Default user friendly name "Cart #id" for example






class Order(BaseModel):
    id: OrderId
    clientId: ClientId
    cartId: CartId
    create_at: datetime.datetime | None = datetime.datetime.now()
    updated_at: datetime.datetime | None = datetime.datetime.now()
    status: Status | None = Status.EMPTY




