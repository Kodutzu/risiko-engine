from pydantic import BaseModel
from ..Constant.Bullet import Bullet
from typing import List, Optional
from ..Effect._Effect import _Effect as Effect

class ShotgunBaseResponse(BaseModel):
    success: bool
    msg: Optional[str] = None
    bullet_type: Optional[Bullet] = None
    damage: int

class shotgunDamageResponse(BaseModel):
    old_damage: int
    new_damage: int
class ShotgunLoad(ShotgunBaseResponse):
    load_in_shell: Optional[bool]
    load_in_chamber: Optional[bool]
    
class ShotgunFireResponse(ShotgunBaseResponse):
    fired: bool
    effects_triggered: List[dict] = []


class ShotgunReloadResponse(ShotgunBaseResponse): 
    total_lives: int
    total_blanks: int
    bullet_lineup: List[Bullet] = []
    chamber_loaded: bool

class ShotgunShellResponse(ShotgunBaseResponse):
   pass

class ShotgunError(BaseModel):
    pass
