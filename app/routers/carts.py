from fastapi import APIRouter, Depends, HTTPException

from ..depend import get_token_header

router = APIRouter(
    prefix="/carts",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


fake_carts_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def read_items():
    return fake_items_db


@router.get("/{cart_id}")
async def read_cart(cart_id: str):
    if cart_id not in fake_carts_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_carts_db[cart_id]["name"], "cart_id": cart_id}


@router.put(
    "/{cart_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_cart(cart_id: str):
    if cart_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the cart: plumbus"
        )
    return {"cart_id": item_id, "name": "The great Plumbus"}