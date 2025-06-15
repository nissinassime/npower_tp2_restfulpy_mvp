import datetime
from typing import List

import DateTime

from models.client import ClientId
from models.product import Product, ProductId
from utils.generate_ids import generate_ids

#Default user friendly name "Cart #id" for example

type CartId = int
type Quantity = int

class Cart(object):
    id: CartId
    clientId: ClientId
    userFriendlyName: str
    create_at: datetime.datetime
    updated_at: datetime.datetime
    items: list[tuple[ProductId, Quantity]]

    def __init__(self, id: CartId, clientId: ClientId, userFriendlyName: str = "My New Cart",
                 items: list[tuple[ProductId, Quantity]] = None) -> None:
        self.id = id # generate_ids()
        self.clientId = clientId
        self.userFriendlyName = userFriendlyName
        self.create_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.items = items or []

    def __str__(self) -> str:
        return f"Cart {self.id} for client {self.clientId} ({self.userFriendlyName})" \
               f" with {len(self.items)} items"
