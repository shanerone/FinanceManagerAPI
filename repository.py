from sqlalchemy import select

from database import ItemORM
from schemas import SItemAdd
from database import new_session


class ItemRepository:
    @classmethod
    async def add_one(cls, item: SItemAdd) -> int:
        async with new_session() as session:
            item_dict = item.model_dump()

            item = ItemORM(**item_dict)
            session.add(item)
            await session.flush()
            await session.commit()
            return item.id

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(ItemORM)
            result  = await session.execute(query)
            item_models = result.scalars().all()
            return item_models
