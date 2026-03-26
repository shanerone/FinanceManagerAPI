from sqlalchemy import select

from database import TransactionORM
from schemas import STransactionAdd, STransaction
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
        transaction = await session.get(TransactionORM, transaction_id)
        if transaction:
            session.delete(transaction)                           
            await session.commit()
            return transaction_id