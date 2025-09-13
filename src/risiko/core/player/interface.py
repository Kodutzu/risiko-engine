from typing import Protocol, runtime_checkable, TYPE_CHECKING


if TYPE_CHECKING:
    from .base import PlayerBase

@runtime_checkable
class PlayerInterface(Protocol):

    @property
    def id(self) -> str: ...

    @property
    def charges(self) -> int:...

    
    def lose_charges(self,amt: int) -> PlayerBase:
        ...

    def gain_charges(self,  amt: int) -> PlayerBase:
        ...
        
