import datetime
from enum import Enum
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import datetime
import enum


#Default user friendly name "Cart #id" for example

type OrderId = int

type ProductId = int

class Product(BaseModel):
    id: ProductId
    name: str
    priceInCents: int # in cents
    quantity: int
    # sku: str

