from typing import Protocol, runtime_checkable, TYPE_CHECKING, Final


@runtime_checkable
class PlayerInterface(Protocol):

    id: str
    charges: int

    
    def _lose_charges(self,amt: int) -> "PlayerInterface":
        ...

    def _gain_charges(self,amt: int) -> "PlayerInterface":
        ...