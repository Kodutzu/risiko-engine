from typing import Optional, Protocol, Type, runtime_checkable
from ..magazine.interface import MagazineInterface
from ..shell.interface import ShellInterface

@runtime_checkable
class ShotgunInterface(Protocol):

    @property
    def id(self) -> str:
        ...
    @property
    def magazine(self) -> MagazineInterface:
        ...

    @property
    def chamber(self) -> Optional[ShellInterface]:
        ...
    
    @chamber.setter
    def chamber(self, shell: Optional[ShellInterface]) -> None:
        ...


            