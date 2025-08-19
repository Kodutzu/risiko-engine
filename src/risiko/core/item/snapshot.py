from pydantic import BaseModel
from ...constants.usable_entity import UsableEntity

class ItemSnapshot(BaseModel):
    entity: UsableEntity