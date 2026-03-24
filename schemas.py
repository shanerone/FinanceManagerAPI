from typing import Optional

from pydantic import BaseModel, Field


class SItemAdd(BaseModel):
    name: str = Field(min_length=1)
    description: Optional[str] = None
    price: float = Field(ge = 1)

class SItem(SItemAdd):
    id: int