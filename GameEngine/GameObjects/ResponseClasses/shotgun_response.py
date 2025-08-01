from dataclasses import dataclass, field
from typing import List, Optional, Literal
from ..Constant.Bullet import Bullet


@dataclass
class ShotgunBaseResponse:
    success: bool
    msg: Optional[str] = None


# @dataclass
# class ShotgunEffectModel:
#     """Replaces raw dict-based effects with structured data"""
#     effect_type: str
#     duration: int


@dataclass
class ShotgunLoadResponse(ShotgunBaseResponse):
    bullet_type: Bullet = None

@dataclass
class ShotgunFireResponse(ShotgunBaseResponse):
    bullet_type: Bullet = None
    damage: int = None

@dataclass
class ShotgunErrorResponse(ShotgunBaseResponse):
    success: Literal[False] = False
    error: Optional[str] = None
