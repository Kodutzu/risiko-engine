from pydantic import BaseModel, Field
from typing import Deque, Union
from collections import deque
from ...constants.shell import Shell
from ..effect.snapshot import EffectorSnapshot


class MagazineSnapshot(BaseModel):

    lives: int = Field(default=4,ge=1, frozen=True)
    blanks: int = Field(default=4,ge=1, frozen=True)
    tube: Deque[Shell] = Field(default_factory=deque)

class ShotgunSnapshot(BaseModel):

    magazine: MagazineSnapshot = Field(default_factory=MagazineSnapshot)
    chambered_shell: Union[Shell,None] = Field(default=None)
    effector: EffectorSnapshot = Field(default_factory=EffectorSnapshot)
    live_dmg: int  = Field(default=1)
    
