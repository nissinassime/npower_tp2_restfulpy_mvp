from fastapi import APIRouter, Depends, HTTPException

from ..depend import get_token_header

router = APIRouter(
    prefix="/products",
    tags=["products"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


fake_products_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def read_products():
    return fake_products_db


@router.get("/{product_id}")
async def read_product(product_id: str):
    if product_id not in fake_products_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_products_db[product_id]["name"], "product_id": product_id}


@router.put(
    "/{product_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_product(product_id: str):
    if product_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the product: plumbus"
        )
    return {"product_id": product_id, "name": "The great Plumbus"}