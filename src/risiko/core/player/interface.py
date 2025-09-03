from abc import ABC, abstractmethod
from ..inventory.interface import InventoryInterface    


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



