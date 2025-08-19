from ..effect.effector import Effector
from ...constants.bullet import Bullet
from .magazine import Magazine
from .shell import Shell
from pydantic import BaseModel, Field, PrivateAttr

class Shotgun(BaseModel):

    magazine: Magazine
    shell: Shell = Field(default_factory=Shell)
    effector: Effector = Field(default_factory=Effector)
    _live_dmg: int = PrivateAttr(default=1)

    class Config:
        arbitrary_types_allowed = True

    def load_chamber(self) -> Bullet:
        
        bullet = self.magazine.take_out_bullet()
        self.shell.load(bullet)

        return bullet
        
    @property
    def live_damage(self) -> int:
        return self._live_dmg 
            
    def set_live_damage(self,new_dmg) -> None:

        if new_dmg < 0: raise ValueError("Damage cannot be negative")
        
        self._live_dmg = new_dmg

    def __repr__(self) -> str:
        return f"Shotgun( magazine={repr(self.magazine)}, shell={repr(self.shell)}, dmg={self._live_dmg}, effects={self.effects.show()})"

