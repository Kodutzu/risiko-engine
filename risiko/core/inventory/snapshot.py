from pydantic import BaseModel
from typing import List
from ...constants.usable_entity import UsableEntity
from ..item.item import Item

class ItemSnapshot(BaseModel):
    entity: UsableEntity

class inventorySnapshot(BaseModel):
    items: List[ItemSnapshot]   
    capacity: int