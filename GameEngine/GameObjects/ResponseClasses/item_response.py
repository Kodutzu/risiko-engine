from dataclasses import dataclass, field
from typing import Optional, Dict, List
from ...GameConstant.bullet import Bullet
from ...GameConstant.item_type import ItemType
from ..Effect._effect import _Effect as Effect  


@dataclass
class ItemAppliedResponse:
    item_name: str 
    user: str = None
    target: str = None
    charges_gain: Optional[int] = None
    current_bullet_type: Optional[Bullet] = None
    damage: Optional[int] = None
    effects_applied: Optional[Dict[Effect, int]] = None
    shell_ejected: Optional[Bullet] = None
    future_bullet: Optional[Bullet] = None