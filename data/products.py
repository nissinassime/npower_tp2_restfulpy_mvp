import datetime
import csv
from pathlib import Path
from typing import List
from models.product import Product, ProductId


class Products:
    db: dict[ProductId, Product]
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def __init__(self):
        self.db = {}
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self) -> str:
        return f"Products(count={len(self.db)})"

    def __repr__(self) -> str:
        return f"Products(db={self.db}, created_at={self.created_at}, updated_at={self.updated_at})"

    def find_product_by_id(self, product_id: ProductId) -> Product | None:
        # return next((p for p in self.db if p.id == product_id), None)
        return self.db.get(product_id, None)

    def add_product_db(self, product: Product) -> bool:
        if self.find_product_by_id(product.id) is not None:
            return False
        self.db.setdefault(product.id, product)
        self.updated_at = datetime.datetime.now()
        return True

    def update_product_db(self, product: Product) -> bool:
        existing = self.find_product_by_id(product.id)
        if existing is None:
            return False
        self.db[product.id] = product
        self.updated_at = datetime.datetime.now()
        return True

    def remove_product_db(self, product_id: int) -> bool:
        product = self.find_product_by_id(product_id)
        if product is None:
            return False
        del self.db[product.id]
        self.updated_at = datetime.datetime.now()
        return True

    def add_product(self,  product_id: int) -> bool:
        existing = self.find_product_by_id( product_id)
        if existing is None:
            return False
        existing.quantity += 1
        self.db.update({existing.id: existing })
        self.updated_at = datetime.datetime.now()
        return True

    def update_product(self,  product_id: int, name: str = None, price_cents: int = None, quantity: int = None) -> bool:
        existing = self.find_product_by_id(product_id)
        if existing is None:
            return False

        if name is not None:
            existing.name = name
        if price_cents is not None:
            existing.priceInCents = price_cents
        if quantity is not None:
            existing.quantity = quantity

        self.updated_at = datetime.datetime.now()
        return True

    def remove_product(self, product_id: int) -> bool:
        existing = self.find_product_by_id(product_id)
        if existing is None:
            return False
        if existing.quantity > 1:
            existing.quantity -= 1
        self.db.update({existing.id: existing })
        self.updated_at = datetime.datetime.now()
        return True

    def load_from_csv(self, file_path: str | Path = None) -> bool:
        if file_path is None:
            file_path = Path(__file__).parent / 'products.csv.txt'
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    product = Product(
                        id=int(row['id']),
                        name=row['name'],
                        priceInCents=int(row['price']),
                        quantity=int(row['quantity']),
                    )
                    self.add_product_db(product)
            return True

        except (FileNotFoundError, ValueError, KeyError) as e:
            print(f"Error loading CSV file: {str(e)}")
            return False
