from pydantic import BaseModel, Field
from typing import List
from ..item.snapshot import ItemSnapshot


class InventorySnapshot(BaseModel):
    item_list: List[ItemSnapshot] =  Field(default_factory=list)
    capacity: int = Field(default=4)