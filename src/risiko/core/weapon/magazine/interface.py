from typing import Deque, Protocol,runtime_checkable
from ..shell.interface import ShellInterface

@runtime_checkable
class MagazineInterface(Protocol):

    @property
    def tube(self) ->  Deque[ShellInterface]:
        ...
    
    @property
    def is_tube_empty(self) ->  bool:
        ...

    @property
    def has_mixed_bullets(self) ->  bool:
        ...
