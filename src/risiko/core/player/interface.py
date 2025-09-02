from typing import Protocol
from ..inventory.interface import InventoryInterface    


class PlayerInterface(Protocol):

    @property
    def id(self) -> str:
        pass

    @property
    def inventory(self) -> InventoryInterface:
        pass
    
    @property
    def charges(self) -> int:
        pass


