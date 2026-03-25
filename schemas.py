from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class SItemAdd(BaseModel):
    name: str = Field(min_length=1)
    description: Optional[str] = None
    price: float = Field(ge = 1)
    model_config = ConfigDict(from_attributes=True)

class SItem(SItemAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)

class SItemId(BaseModel):
    ok: bool = True
    item_id: int