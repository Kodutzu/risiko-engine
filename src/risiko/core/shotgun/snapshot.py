from pydantic import BaseModel, Field
from typing import List, Tuple, Union
from ...constants.bullet import Bullet
from ..effect.snapshot import EffectorSnapshot

class ShotgunSnapshot(BaseModel):

    magazine: List[Bullet] = Field(default_factory=list)
    shell: Union[Bullet,None] = Field(default=None)
    effector: EffectorSnapshot = Field(default_factory=EffectorSnapshot)
    live_dmg: int  = Field(default=1)
    
