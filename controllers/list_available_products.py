from typing import Tuple, Dict
from data.productsdao import ProductsDao


def get_available_products() -> Tuple[Dict[str, any], ...]:
    """
    Get products from Products.db and return a tuple of available products.

    Returns:
        Tuple[Dict[str, any], ...]: Tuple containing product information dictionaries
    """
    try:
        products = []
        products_db = ProductsDao()
        products_db.load_from_csv()

        for product in products_db.db.values():
            products.append({
                'id': product.id,
                'name': product.name,
                'price': float(product.priceInCents) / 100,
                'quantity': product.quantity
            })

        return tuple(products)

    except Exception as e:
        print(f"Error reading products: {str(e)}")
        return tuple()
