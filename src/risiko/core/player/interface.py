from abc import ABC, abstractmethod
from ..payload.inventory.interface import InventoryInterface    


class PlayerInterface(ABC):

    @property
    @abstractmethod
    def id(self) -> str:
        pass

    @property
    @abstractmethod
    def inventory(self) -> InventoryInterface:
        pass
    
    @property
    @abstractmethod
    def charges(self) -> int:
        pass

    @abstractmethod
    def gain_charge(self, amt: int) -> None:
        pass

    @abstractmethod
    def lose_charge(self, amt: int) -> None:
        pass



