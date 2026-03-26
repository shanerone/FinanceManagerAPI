from sqlalchemy import select
from typing import Optional

from database import TransactionORM
from schemas import STransactionAdd, STransaction, STransactionUpdate
from database import new_session


class TransactionRepository:
    @classmethod
    async def add_one(cls, transaction: STransactionAdd) -> int:
        async with new_session() as session:
            transaction_dict = transaction.model_dump()

            transaction = TransactionORM(**transaction_dict)
            session.add(transaction)
            await session.flush()
            await session.commit()
            return transaction.id

    @classmethod
    async def find_all(cls) -> list[STransaction]:
        async with new_session() as session:
            query = select(TransactionORM)
            result  = await session.execute(query)
            transaction_models = result.scalars().all()
            transaction_schemas = [STransaction.model_validate(transaction_model) for transaction_model in transaction_models]
            return transaction_schemas

    @classmethod
    async def delete_one(cls, transaction_id: int):
        async with new_session() as session:
            transaction = await session.get(TransactionORM, transaction_id)
            if transaction:
                session.delete(transaction)                           
                await session.commit()
                return transaction_id

    @classmethod
    async def update_one(cls, transaction_id: int, transaction_data: STransactionUpdate) -> Optional[STransaction]:
        async with new_session() as session:
            transaction = await session.get(TransactionORM, transaction_id)
            if transaction:
                update_data = transaction_data.model_dump(exclude_unset=True)
                for field, value in update_data.items():
                    setattr(transaction, field, value)
                await session.commit()
                await session.refresh(transaction)
                return STransaction.model_validate(transaction)