from pydantic import BaseModel
from typing import List
from ..item.snapshot import ItemSnapshot


class InventorySnapshot(BaseModel):
    item_list: List[ItemSnapshot]   
    capacity: int