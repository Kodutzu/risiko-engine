from abc import ABC, abstractmethod
from ..inventory.interface import InventoryInterface    


class PlayerInterface(ABC):

    @property
    @abstractmethod
    def id(self) -> str: ...


    @property
    @abstractmethod
    def inventory(self) -> InventoryInterface: ...
    
    @property
    @abstractmethod
    def charges(self) -> int:...

    @charges.setter
    @abstractmethod
    def charges(self, value: int) -> None: ...



