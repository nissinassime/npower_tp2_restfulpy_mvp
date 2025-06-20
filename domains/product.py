

type ProductId = int

class Product(object):
    id: ProductId
    name: str
    priceInCents: int # in cents
    quantity: int
    # sku: str

    def __init__(self, id: ProductId,  name: str, priceInCents: int, quantity: int = 0):  # sku: str,
        self.id = id
        self.name = name
        self.priceInCents = priceInCents
        self.quantity = quantity
        # self.sku = sku

    def __str__(self) -> str:
        return f"Product(id={self.id}, name='{self.name}', price={self.priceInCents})" #, quantity={self.quantity})" # (SKU: {self.sku})"

    def __repr__(self) -> str:
        return f"Product(id={self.id}, name='{self.name}', price={self.priceInCents})" #, quantity={self.quantity})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self.id == other.id # and self.sku == other.sku


