from pydantic import BaseModel
from ...core.payload.item_type import ItemType

class ItemSnapshot(BaseModel):
    entity: ItemType