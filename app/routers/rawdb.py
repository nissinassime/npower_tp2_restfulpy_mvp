from fastapi import APIRouter, Depends, HTTPException

from ..depend import get_token_header

router = APIRouter(
    prefix="/rawdbs",
    tags=["rawdbs"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


fake_rawdbs_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def read_rawdbs():
    return fake_rawdbs_db


@router.get("/{rawdb_id}")
async def read_rawdb(rawdb_id: str):
    if rawdb_id not in fake_rawdbs_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_rawdbs_db[rawdb_id]["name"], "rawdb_id": rawdb_id}


@router.put(
    "/{rawdb_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_rawdb(rawdb_id: str):
    if rawdb_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the rawdb: plumbus"
        )
    return {"rawdb_id": rawdb_id, "name": "The great Plumbus"}