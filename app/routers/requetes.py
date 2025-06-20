from fastapi import APIRouter, Depends, HTTPException

from ..depend import get_token_header

router = APIRouter(
    prefix="/requetes",
    tags=["requetes"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


fake_requetes_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def read_requetes():
    return fake_requetes_db


@router.get("/{requete_id}")
async def read_requete(requete_id: str):
    if requete_id not in fake_requetes_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_requetes_db[requete_id]["name"], "requete_id": requete_id}


@router.put(
    "/{requete_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_requete(requete_id: str):
    if requete_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the requete: plumbus"
        )
    return {"requete_id": requete_id, "name": "The great Plumbus"}