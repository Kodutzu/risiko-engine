from dataclasses import dataclass
from typing import List, Optional, Literal
from ...GameConstant.bullet import Bullet


@dataclass
class ShotgunResponse:
    bullet_type: Optional[Bullet] = None
    damage: Optional[int] =  None


