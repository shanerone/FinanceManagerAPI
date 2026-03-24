from typing import Annotated

from fastapi import APIRouter, Depends

from repository import ItemRepository
from schemas import SItemAdd

router = APIRouter(
    prefix='/items',
    tags = ['Элементы']
)

@router.get("/health")
async def get_health():
    return {"status": "ok"}

@router.post("")
async def items_add(item: Annotated[SItemAdd, Depends()]):
    item_id = await ItemRepository.add_one(item)
    return {"ok": True, "item_id": item_id}

@router.get("")
async def items_get():
    items = await ItemRepository.find_all()
    return {'data': items}