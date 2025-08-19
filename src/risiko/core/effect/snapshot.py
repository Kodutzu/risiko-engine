from pydantic import BaseModel, Field
from typing import List
from ...constants.usable_entity import UsableEntity

class EffectSnapshot(BaseModel):
    entity: UsableEntity 
    remaining_turns: int
    
class EffectorSnapshot(BaseModel):
    effects: List[EffectSnapshot] = Field(default_factory=list)