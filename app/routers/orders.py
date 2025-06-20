from fastapi import APIRouter, Depends, HTTPException

from ..depend import get_token_header

router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


fake_orders_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def read_orders():
    return fake_orders_db


@router.get("/{order_id}")
async def read_order(order_id: str):
    if order_id not in fake_orders_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_orders_db[order_id]["name"], "order_id": order_id}


@router.put(
    "/{order_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_order(order_id: str):
    if order_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the order: plumbus"
        )
    return {"order_id": order_id, "name": "The great Plumbus"}