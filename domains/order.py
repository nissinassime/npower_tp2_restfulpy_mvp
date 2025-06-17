import datetime
from enum import Enum
from typing import List

import DateTime

from domains.cart import CartId
from domains.client import ClientId
from domains.product import Product, ProductId
# from utils.generate_ids import generate_ids

#Default user friendly name "Cart #id" for example

type OrderId = int

class Status(Enum):
    EMPTY = "EMPTY"
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class Order(object):
    id: OrderId
    clientId: ClientId
    cartId: CartId
    create_at: datetime.datetime
    updated_at: datetime.datetime
    status: Status

    def __init__(self, id: OrderId, clientId: ClientId, cartId: CartId, status: Status = Status.EMPTY):
        self.id = id
        self.clientId = clientId
        self.cartId: cartId
        self.create_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.status = status

    def __str__(self) -> str:
        return f"Order {self.id} for client {self.clientId} ({self.cartId})" \
               f" - Status: {self.status}"

    def __repr__(self) -> str:
        return f"Order(id={self.id}, clientId={self.clientId}, userFriendlyName={self.cartId}, status={self.status})"




