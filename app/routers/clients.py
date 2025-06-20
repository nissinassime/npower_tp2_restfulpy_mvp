from fastapi import APIRouter, Depends, HTTPException

from ..depend import get_token_header

router = APIRouter(
    prefix="/clients",
    tags=["clients"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


fake_clients_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def read_clients():
    return fake_clients_db


@router.get("/{client_id}")
async def read_client(client_id: str):
    if client_id not in fake_clients_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_clients_db[client_id]["name"], "client_id": client_id}


@router.put(
    "/{client_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_client(client_id: str):
    if client_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the client: plumbus"
        )
    return {"client_id": client_id, "name": "The great Plumbus"}