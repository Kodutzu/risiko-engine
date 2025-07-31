from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Union
from ..Constant.Bullet import Bullet


class ShotgunBaseResponse(BaseModel):
    success: bool = Field(..., description="Was the operation successful?")
    msg: Optional[str] = Field(None, description="Human-readable result message")

#
class ShotgunEffectModel(BaseModel):
    """Replaces raw dict-based effects with structured data"""
    effect_type: str
    duration: int


class ShotgunLoadResponse(ShotgunBaseResponse):
    bullet_type: Optional[Bullet]
    bullet_in_shell: Optional[bool]
    shell_in_chamber: Optional[bool]


class ShotgunFireResponse(ShotgunBaseResponse):
    bullet_type: Optional[Bullet]
    damage: Optional[int]
    fired: bool = False
    # effects_triggered: List[ShotgunEffectModel] = []


class ShotgunReloadResponse(ShotgunBaseResponse):
    total_lives: int
    total_blanks: int
    bullet_lineup: List


class ShotgunShellResponse(ShotgunBaseResponse):
    bullet_type: Optional[Bullet]


class ShotgunDamageUpdate(BaseModel):
    old_damage: int
    new_damage: int
class ShotgunErrorResponse(ShotgunBaseResponse):
    success: Literal[False] = False
    error: str = Field(None, description="Error message, if any")


