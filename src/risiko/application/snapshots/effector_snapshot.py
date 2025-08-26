from pydantic import BaseModel, Field
from typing import List
from .effect_snapshot import EffectSnapshot


class EffectorSnapshot(BaseModel):
    effect_list: List[EffectSnapshot] = Field(default_factory=list)