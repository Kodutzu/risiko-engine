from dataclasses import dataclass, field
from typing import Optional, Dict
from ...GameConstant.bullet import Bullet
from ..Effect._effect import _Effect as Effect  
from .item_response import ItemAppliedResponse

@dataclass
class PlayerShootResponse:
    bullet_type: Optional[Bullet] = None
    damage: Optional[int] = None


@dataclass
class ItemUsageResponse:
    item_applied: ItemAppliedResponse