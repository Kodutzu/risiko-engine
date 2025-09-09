from typing import override, Optional, final
from attrs import define, field, Factory, setters
from attrs.validators import instance_of, gt,optional

from ..shell.interface import ShellInterface
from ..magazine.base import MagazineBase
from .interface import ShotgunInterface, MagazineInterface


@define
class ShotgunBase(ShotgunInterface):

    _id: str = field(converter=str,on_setattr=setters.frozen, alias="Shotgun_id")
    _magazine: MagazineInterface = field(default=Factory(MagazineBase),validator=(instance_of(MagazineInterface)), alias="magazine")
    _chamber: Optional[ShellInterface] = field(default=None, alias="chamber", validator=optional(instance_of(ShellInterface)))
        
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
    def chamber(self) -> Optional[ShellInterface]:
        return self._chamber
    
    @chamber.setter
    @override
    @final
    def chamber(self, shell: Optional[ShellInterface]) -> None:
        self._chamber = shell
    

    
