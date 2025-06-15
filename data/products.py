import datetime
from typing import List
from models.product import Product


class Products:
    db: List[Product]
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def __init__(self):
        self.db = []
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self) -> str:
        return f"Products(count={len(self.db)})"

    def __repr__(self) -> str:
        return f"Products(db={self.db}, created_at={self.created_at}, updated_at={self.updated_at})"

    def find_product_by_id(self, product_id: int) -> Product | None:
        return next((p for p in self.db if p.id == product_id), None)

    def add_product(self, product: Product) -> bool:
        if self.find_product_by_id(product.id) is not None:
            return False
        self.db.append(product)
        self.updated_at = datetime.datetime.now()
        return True

    def update_product(self, product: Product) -> bool:
        existing = self.find_product_by_id(product.id)
        if existing is None:
            return False
        self.db[self.db.index(existing)] = product
        self.updated_at = datetime.datetime.now()
        return True

    def remove_product(self, product_id: int) -> bool:
        product = self.find_product_by_id(product_id)
        if product is None:
            return False
        self.db.remove(product)
        self.updated_at = datetime.datetime.now()
        return True
