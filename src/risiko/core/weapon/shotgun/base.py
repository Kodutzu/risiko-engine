from typing import override, Optional, final
from attrs import define, field, Factory, setters
from attrs.validators import instance_of, gt,optional

from ..shell import Shell
from ..magazine.base import MagazineBase
from .interface import ShotgunInterface, MagazineInterface


@define
class ShotgunBase(ShotgunInterface):

    _id: str = field(converter=str,on_setattr=setters.frozen, alias="Shotgun_id")
    _magazine: MagazineInterface = field(default=Factory(MagazineBase),validator=(instance_of(MagazineInterface)), alias="magazine")
    _chamber: Optional[Shell] = field(default=None, alias="chamber", validator=optional(instance_of(Shell)))
    _damage: int = field(default=1, converter=int, validator=gt(0), alias="live_damage")
        
    @property
    @override
    @final
    def id(self) -> str:
        return self._id
    
    @property
    @override
    @final
    def magazine(self) -> MagazineInterface:
        return self._magazine
    
    @property
    @override
    @final
    def chamber(self) -> Optional[Shell]:
        return self._chamber

    @property
    @override
    @final
    def live_damage(self) -> int:
        return self._damage
    
    @chamber.setter
    @override
    @final
    def chamber(self, shell: Optional[Shell]) -> None:
        self._chamber = shell
    
    @live_damage.setter
    @override
    @final
    def live_damage(self, value) -> None:
        
        self._damage  = value

    
