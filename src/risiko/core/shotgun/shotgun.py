from ..effect.effector import Effector
from ...constants.shell import Shell
from .magazine import Magazine
from typing import Union
from pydantic import BaseModel, Field, PrivateAttr

class Shotgun(BaseModel):

    magazine: Magazine = Field(default_factory=Magazine)
    effector: Effector = Field(default_factory=Effector)
    _chamber: Union[Shell, None] = Field(default=None)
    _live_dmg: int = PrivateAttr(default=1)
        
    @property
    def chamber(self) -> Union[Shell, None]:
        return self._chamber
    
    @property
    def live_damage(self) -> int:
        return self._live_dmg 

    
    def load_chamber(self) -> Shell:
        """Loads the next shell type from the magazine into the chamber."""
        shell_type = self.magazine.take_out_bullet()
        self.chamber = shell_type
        return self.chamber
            
    def set_live_damage(self,new_dmg) -> None:

        if new_dmg < 0: raise ValueError("Damage cannot be negative")
        
        self._live_dmg = new_dmg

    def __repr__(self) -> str:
        return f"Shotgun( magazine={repr(self.magazine)}, shell={repr(self.shell)}, dmg={self._live_dmg}, effects={self.effects.show()})"

