from pydantic import BaseModel
from typing import List
from ...constants.usable_entity import UsableEntity
from ..item.snapshot import ItemSnapshot


class inventorySnapshot(BaseModel):
    items: List[ItemSnapshot]   
    capacity: int