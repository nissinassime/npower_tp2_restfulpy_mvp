import datetime
from enum import Enum
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import datetime
import enum

from domains.product import ProductId


#Default user friendly name "Cart #id" for example



class Product(BaseModel):
    id: ProductId
    name: str
    priceInCents: int # in cents
    quantity: int | None = 1
    # sku: str

