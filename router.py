from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from schemas import STransactionId, STransactionUpdate
from repository import TransactionRepository
from schemas import STransactionAdd, STransaction

router = APIRouter(
    prefix='/transactions',
    tags = ['Транзакции']
)

@router.get("/health")
async def get_health():
    return {"status": "ok"}

@router.post("")
async def transactions_add(transaction: Annotated[STransactionAdd, Depends()]) -> STransactionId:
    transaction_id = await TransactionRepository.add_one(transaction)
    return {"ok": True, "transaction_id": transaction_id}

@router.get("")
async def transactions_get() -> list[STransaction]:
    transactions = await TransactionRepository.find_all()
    return transactions

@router.delete("")
async def transactions_del(transaction_id: int) -> STransactionId:
    await TransactionRepository.delete_one(transaction_id)
    return {"ok": True}

@router.put("/{transaction_id}")
async def transaction_update(transaction_id: int, transaction_data: STransactionUpdate) -> STransaction:
    updated_transaction = await TransactionRepository.update_one(transaction_id, transaction_data)
    if not updated_transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return updated_transaction
