from dataclasses import dataclass, field
from typing import Optional, Dict
from ..Constant.Bullet import Bullet
from ..Effect._Effect import _Effect as Effect  

@dataclass
class PlayerShootResponse:
    success: Optional[bool] = None
    msg: Optional[str] = None
    bullet_type: Optional[Bullet] = None
    damage: Optional[int] = None
    fired: bool = False


@dataclass
class ItemUsageResponse:
    item_name: str
    used_by: str  # player ID or name
    target: str  # target ID or name
    success: bool
    msg: str
    effect_applied: Optional[str] = None  # e.g., "CUFFED", "DEFLECT", etc.
