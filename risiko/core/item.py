from pydantic import BaseModel
from ..constants.usable_entity import UsableEntity

class Item(BaseModel):
    entity: UsableEntity

    def __repr__(self) -> str:
        return f"Item(entity={self.entity.name})"


