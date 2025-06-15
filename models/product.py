

type ProductId = int

class Product:
    id: ProductId
    name: str
    priceInCents: int # in cents
    # sku: str

    def __init__(self, id: ProductId,  name: str, priceInCents: int) -> None:  # sku: str,
        self.id = id
        self.name = name
        self.priceInCents = priceInCents
        # self.sku = sku

    def __str__(self) -> str:
        return f"{self.name}" # (SKU: {self.sku})"

    def __repr__(self) -> str:
        return f"Product(id={self.id}, name='{self.name}', price={self.priceInCents})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self.id == other.id # and self.sku == other.sku
