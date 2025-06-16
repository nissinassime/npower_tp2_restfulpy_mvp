import datetime
import csv
import json
from pathlib import Path
from typing import List, Dict

from domains.cart import Cart, Quantity, CartId
from domains.client import ClientId
from domains.product import ProductId


# from models.product import Product, ProductId

# NOTE cart_id == client_id

UNKNOWN_PRODUCT_ID = 999999

class CartsDao:
    db: dict[ClientId, Cart]
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def __init__(self):
        self.db = {}
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self) -> str:
        return f" Carts(count={len(self.db)})"

    def __repr__(self) -> str:
        return f" Carts(db={self.db}, created_at={self.created_at}, updated_at={self.updated_at})"

    def find_cart_by_client_id(self, client_id: ClientId) -> Cart | None:
        # return next((p for p in self.db if p.id == cart_id), None)
        return self.db.get(client_id, None)

    def find_cart_by_id(self, client_id: ClientId) -> Cart | None:
        return self.find_cart_by_client_id(client_id)

    def load_from_json(self, file_path: str) -> bool:
        try:
            with open(file_path, 'r') as f:
                carts_data = json.load(f)
                print(carts_data)
                for carts_id, cart_data in carts_data.items():
                    print(carts_id, ' ->>> ', cart_data)
                    cart = Cart(
                        id=carts_id,
                        clientId=carts_id,
                        userFriendlyName=cart_data.get('userFriendlyName', 'Mon Nouveau Panier Aujourdhui {id}'),
                        items=[(prodid, qtty) for prodid in cart_data.get('productId', UNKNOWN_PRODUCT_ID) for qtty in cart_data.get('quantity', 0) ]
                    )
                    self.db[cart.clientId] = cart
                self.updated_at = datetime.datetime.now()
            return True
        except (FileNotFoundError, json.JSONDecodeError):
            return False

    # def add_cart_db(self, cart: Cart) -> bool:
    #     if self.find_cart_by_id(cart.id) is not None:
    #         return False
    #     self.db[cart.id]= cart
    #     self.updated_at = datetime.datetime.now()
    #     return True
    #
    # def update_cart_db(self, cart: Cart) -> bool:
    #     existing = self.find_cart_by_id(cart.id)
    #     if existing is None:
    #         return False
    #     self.db[cart.id] = cart
    #     self.updated_at = datetime.datetime.now()
    #     return True
    #
    # def remove_cart_db(self, cart_id: int) -> bool:
    #     cart = self.find_cart_by_id(cart_id)
    #     if cart is None:
    #         return False
    #     del self.db[cart.id]
    #     self.updated_at = datetime.datetime.now()
    #     return True
    #
    # def add_cart(self,  cart_id: int) -> bool:
    #     existing = self.find_cart_by_id( cart_id)
    #     if existing is None:
    #         return False
    #     existing.quantity += 1
    #     self.db.update({existing.id: existing })
    #     self.updated_at = datetime.datetime.now()
    #     return True
    #
    # def update_cart(self,  cart_id: int, name: str = None, price_cents: int = None, quantity: int = None) -> bool:
    #     existing = self.find_cart_by_id(cart_id)
    #     if existing is None:
    #         return False
    #
    #     if name is not None:
    #         existing.name = name
    #     if price_cents is not None:
    #         existing.priceInCents = price_cents
    #     if quantity is not None:
    #         existing.quantity = quantity
    #
    #     self.updated_at = datetime.datetime.now()
    #     return True
    #
    # def remove_cart(self, cart_id: int) -> bool:
    #     existing = self.find_cart_by_id(cart_id)
    #     if existing is None:
    #         return False
    #     if existing.quantity > 1:
    #         existing.quantity -= 1
    #     self.db.update({existing.id: existing })
    #     self.updated_at = datetime.datetime.now()
    #     return True