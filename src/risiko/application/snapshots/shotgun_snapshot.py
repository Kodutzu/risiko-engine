from pydantic import BaseModel, Field
from typing import Deque, Union
from collections import deque
from ...core.weapon.shell import Shell
from ...application.snapshots.effector_snapshot import EffectorSnapshot


class MagazineSnapshot(BaseModel):

    tube: Deque[Shell] = Field(default_factory=deque)
    lives: int = Field(default=4,ge=1, frozen=True)
    blanks: int = Field(default=4,ge=1, frozen=True)
 

class ShotgunSnapshot(BaseModel):

    magazine: MagazineSnapshot = Field(default_factory=MagazineSnapshot)
    chambered_shell: Union[Shell,None] = Field(default=None)
    effector: EffectorSnapshot = Field(default_factory=EffectorSnapshot)
    live_damage: int  = Field(default=1)
    
