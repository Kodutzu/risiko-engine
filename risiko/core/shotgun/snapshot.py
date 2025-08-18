from pydantic import BaseModel, Field
from typing import List, Tuple, Union
from ...constants.bullet import Bullet
from ..effect.effect import Effect

class ShotgunSnapshot(BaseModel):

    magazine: List[Bullet] = Field(default_factory=list)
    shell: Union[Bullet,None] = Field(default=None)
    live_dmg: int  = Field(default=1)
    effects: List[Tuple[Effect,int]] = Field(default_factory=list)
