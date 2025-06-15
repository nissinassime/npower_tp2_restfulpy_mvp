import datetime
import csv
from pathlib import Path
from typing import List

from models.client import Client, ClientId
from models.product import Product, ProductId


class Clients:
    db: dict[ClientId, Client]
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def __init__(self):
        self.db = {}
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self) -> str:
        return f"Clients(count={len(self.db)})"

    def __repr__(self) -> str:
        return f"Clients(db={self.db}, created_at={self.created_at}, updated_at={self.updated_at})"

    def find_client_by_id(self, client_id: ClientId) -> Client | None:
        # return next((p for p in self.db if p.id == product_id), None)
        return self.db.get(client_id, None)

    def add_client_db(self, client: Client) -> bool:
        if self.find_client_by_id(client.id) is not None:
            return False
        self.db.setdefault(client.id, client)
        self.updated_at = datetime.datetime.now()
        return True

    def update_client_db(self, client: Client) -> bool:
        existing = self.find_client_by_id(client.id)
        if existing is None:
            return False
        self.db[client.id] = client
        self.updated_at = datetime.datetime.now()
        return True

    def remove_client_db(self, client: Client) -> bool:
        product = self.find_client_by_id(client.id)
        if product is None:
            return False
        del self.db[product.id]
        self.updated_at = datetime.datetime.now()
        return True



    def load_from_csv(self, file_path: str | Path = None) -> bool:
        if file_path is None:
            file_path = Path(__file__).parent / 'clients.csv.txt'
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    client = Client(
                        id=int(row['id']),
                        firstName=row['firstName'],
                        lastName=row['lastName'],
                        # middleName=row['middleName'],
                        dateOfBirth=row['dateOfBirth'],
                    )
                    self.add_client_db(client)
            return True

        except (FileNotFoundError, ValueError, KeyError) as e:
            print(f"Erreure ficher CSV: {str(e)}")
            return False
