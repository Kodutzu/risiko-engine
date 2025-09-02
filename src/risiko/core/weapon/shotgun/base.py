from ..shell import Shell
from ..magazine.base import MagazineBase
from typing import Union, override
from attrs import define, field
from .interface import ShotgunInterface, MagazineInterface
from .validator import live_dmg_checker

@define
class ShotgunBase(ShotgunInterface):

    _magazine: MagazineInterface = field(factory=MagazineBase, alias="magazine")
    _chamber: Union[Shell, None] = field(default=None, alias="chamber")
    _live_damage: int = field(default=1, validator=live_dmg_checker, alias="live_damage")
        

    @property
    @override
    def magazine(self) -> MagazineInterface:
        return self._magazine
    
    @property
    @override
    def chamber(self) -> Union[Shell, None]:
        return self._chamber
    
    @property
    @override
    def live_damage(self) -> int:
        return self._live_damage
    
    @live_damage.setter
    def live_damage(self, value) -> None:
        
        self._live_damage  = value

    
