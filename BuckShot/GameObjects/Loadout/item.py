from pydantic import BaseModel
from ...GameConstant.usable_entity import UsableEntity

class Item(BaseModel):
    type_of: UsableEntity


