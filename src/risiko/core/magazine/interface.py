from typing import Deque, Protocol,runtime_checkable, TYPE_CHECKING, Tuple
from ..shell.interface import ShellInterface

if TYPE_CHECKING:
    from .base import MagazineBase

@runtime_checkable
class MagazineInterface(Protocol):

    @property
    def tube(self) ->  Deque[ShellInterface]:
        ...
    
    @property
    def is_empty(self) ->  bool:
        ...

    def load_round(self,lives:int, blanks:int) -> "MagazineBase":
        ...
    
    def eject_shell(self) -> Tuple[ShellInterface, "MagazineBase"]:
        ...
    
    def clear(self) -> "MagazineBase":
        ...


     


