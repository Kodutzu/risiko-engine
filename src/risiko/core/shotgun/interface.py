from typing import Optional, Protocol, TYPE_CHECKING, runtime_checkable, Tuple
from ..magazine.interface import MagazineInterface
from ..shell.interface import ShellInterface

if TYPE_CHECKING:
    from .base import ShotgunBase

@runtime_checkable
class ShotgunInterface(Protocol):

    @property
    def magazine(self) -> MagazineInterface:
        ...

    @property
    def chamber(self) -> Optional[ShellInterface]:
        ...

    def load_chamber(self) -> "ShotgunBase":
        ...
        
    
    def unload_chamber(self) -> "ShotgunBase":
        ...

    
    def fire(self) -> Tuple[ShellInterface, "ShotgunBase"]:
        ...

