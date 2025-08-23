from pydantic import BaseModel, Field
from typing import List
from ...constants.usable_entity import UsableEntity
from ..effect.snapshot import EffectSnapshot


class EffectorSnapshot(BaseModel):
    effect_list: List[EffectSnapshot] = Field(default_factory=list)