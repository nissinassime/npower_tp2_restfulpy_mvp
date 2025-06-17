import datetime
from typing import List

import DateTime

from domains.client import ClientId
from domains.product import Product, ProductId
# from utils.generate_ids import generate_ids

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

    def __init__(self, id: CartId,
                 clientId: ClientId,
                 userFriendlyName: str = "Mon Nouveau Panier",
                 items: list[tuple[ProductId, Quantity]] = []):
        self.id = clientId # generate_ids()
        self.clientId = clientId
        self.userFriendlyName = userFriendlyName
        self.create_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.items = items or []

    def __str__(self) -> str:
        return f"Cart {self.id} for client {self.clientId} ({self.userFriendlyName})" \
               f" with {(self.items)} items"

    # return f"Cart {self.id} for client {self.clientId} ({self.userFriendlyName})" \
    #        f" with {len(self.items)} items"

    def __repr__(self) -> str:
        return f"Cart(id={self.id}, clientId={self.clientId}, userFriendlyName={self.userFriendlyName}, items={self.items})"


    def find_product_by_id(self, product_id: ProductId) -> int | None:
        existing_idx = None
        for idx, e in enumerate(self.items):
            if e[0] == product_id:
                existing_idx = idx
                break
        return existing_idx


    def add_products(self, product_id: ProductId, quantity: Quantity = 1) -> bool:
        if quantity <= 0:
            return False
        existing_idx = self.find_product_by_id(product_id)
        if existing_idx is not None:
            self.items[existing_idx] = (product_id, self.items[existing_idx][1] + quantity)
        else:
            self.items.append((product_id, quantity))

        self.updated_at = datetime.datetime.now()
        return True
