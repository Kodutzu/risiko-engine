from pydantic import BaseModel
from ...constants.usable_entity import UsableEntity

class EffectSnapshot(BaseModel):
    entity: UsableEntity 
    remaining_turns: int
