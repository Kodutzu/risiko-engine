from ...constants.shell import Shell
from .magazine import MagazineBase
from typing import Union
from attrs import define, field
from .interface import ShotgunInterface, MagazineInterface
from .validator import live_dmg_checker

@define
class ShotgunBase(ShotgunInterface):

    magazine: MagazineInterface = field(factory=MagazineBase)
    _chamber: Union[Shell, None] = field(default=None)
    _live_dmg: int = field(default=1, validator=live_dmg_checker)
        
    @property
    def chamber(self) -> Union[Shell, None]:
        return self._chamber
    
    @property
    def live_damage(self) -> int:
        return self._live_dmg 

    
    def load_chamber(self) -> Shell:
        """Loads the next shell type from the magazine into the chamber."""
        shell_type = self.magazine.take_out_bullet()
        self._chamber = shell_type
        return self._chamber
            
    def set_live_damage(self,new_dmg) -> None:

        if new_dmg < 0: raise ValueError("Damage cannot be negative")
        
        self._live_dmg = new_dmg