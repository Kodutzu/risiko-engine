from pydantic import BaseModel, Field
from typing import List, Tuple, Union
from ...constants.bullet import Bullet
from ..effect.snapshot import EffectorSnapshot


class MagazineSnapshot(BaseModel):

    lives: int = Field(default=4,ge=1, frozen=True)
    blanks: int = Field(default=4,ge=1, frozen=True)
    tube: List[Bullet] = Field(default_factory=list)

class ShotgunSnapshot(BaseModel):

    magazine: MagazineSnapshot = Field(default_factory=MagazineSnapshot)
    current_shell: Union[Bullet,None] = Field(default=None)
    previous_shell: Union[Bullet,None] = Field(default=None)
    effector: EffectorSnapshot = Field(default_factory=EffectorSnapshot)
    live_dmg: int  = Field(default=1)
    
