from pydantic import BaseModel
from ..constants.usable_entity import UsableEntity

class Item(BaseModel):
    type_of: UsableEntity


