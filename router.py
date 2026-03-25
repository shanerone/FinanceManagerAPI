from typing import Annotated

from fastapi import APIRouter, Depends

from schemas import SItemId
from repository import ItemRepository
from schemas import SItemAdd, SItem

router = APIRouter(
    prefix='/items',
    tags = ['Элементы']
)

@router.get("/health")
async def get_health():
    return {"status": "ok"}

@router.post("")
async def items_add(item: Annotated[SItemAdd, Depends()]) -> SItemId:
    item_id = await ItemRepository.add_one(item)
    return {"ok": True, "item_id": item_id}

@router.get("")
async def items_get() -> list[SItem]:
    items = await ItemRepository.find_all()
    return items

@router.delete("")
async def items_del(itemd_id: int) -> SItemId:
    await ItemRepository.delete_one(itemd_id)
    return {"ok": True}