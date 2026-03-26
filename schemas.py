from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class STransactionAdd(BaseModel):
    amount: float = Field(ge = 1)
    description: Optional[str] = None
    type: str
    category_id: Optional[int] = None
    user_id: int
    date: Optional[str] = None

class STransaction(STransactionAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)

class STransactionId(BaseModel):
    ok: bool = True
    transaction_id: int