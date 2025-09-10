from typing import override, Optional, final, Final, Type
from attrs import define, field, Factory,setters
from attrs.validators import instance_of

from ..shell.interface import ShellInterface
from .interface import MagazineInterface

@define
class ShotgunBase:

    id: Final[str] = field(alias="Shotgun_id", converter=str, on_setattr=setters.frozen)
    magazine: MagazineInterface = field(validator=instance_of(MagazineInterface))
    chamber: Optional[ShellInterface] = field(default=None, validator=instance_of((ShellInterface, type(None))))
    
