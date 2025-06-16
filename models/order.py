import datetime
from enum import Enum
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import datetime
import enum


from domains.client import ClientId
from domains.order import Status
from domains.product import Product, ProductId
from utils.generate_ids import generate_ids

#Default user friendly name "Cart #id" for example

type OrderId = int




class Order(BaseModel):
    id: OrderId
    clientId: ClientId
    userFriendlyName: str | None
    create_at: datetime.datetime | None
    updated_at: datetime.datetime | None
    status: Status | None




