from fastapi import APIRouter, Depends, HTTPException

from ..depend import get_token_header

router = APIRouter(
    prefix="/statistiques",
    tags=["statistiques"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


fake_statistiques_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def read_statistiques():
    return fake_statistiques_db


@router.get("/{statistique_id}")
async def read_statistique(statistique_id: str):
    if statistique_id not in fake_statistiques_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_statistiques_db[statistique_id]["name"], "statistique_id": statistique_id}


@router.put(
    "/{statistique_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_statistique(statistique_id: str):
    if statistique_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the statistique: plumbus"
        )
    return {"statistique_id": statistique_id, "name": "The great Plumbus"}