from pydantic import BaseModel
from ..constant.usable_entity import UsableEntity

class Item(BaseModel):
    type_of: UsableEntity


