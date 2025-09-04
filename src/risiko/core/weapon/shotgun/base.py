from typing import override, Optional
from attrs import define, field
from attrs.validators import instance_of, gt

from ..shell import Shell
from ..magazine.base import MagazineBase
from .interface import ShotgunInterface, MagazineInterface


@define
class ShotgunBase(ShotgunInterface):

    _magazine: Optional[MagazineInterface] = field(factory=MagazineBase,validator=instance_of(MagazineInterface), alias="magazine")
    _chamber: Optional[Shell] = field(default=None, alias="chamber")
    _damage: Optional[int] = field(default=1, converter=int, validator=gt(0), alias="live_damage")
        

    @property
    @override
    def magazine(self) -> MagazineInterface:
        return self._magazine
    
    @property
    @override
    def chamber(self) -> Optional[Shell]:
        return self._chamber

    @property
    @override
    def live_damage(self) -> int:
        return self._damage
    
    @chamber.setter
    @override
    def chamber(self, shell:Shell) -> None:
        self._chamber = shell
    
    @live_damage.setter
    @override
    def live_damage(self, value) -> None:
        
        self._damage  = value

    
