from abc import ABC, abstractmethod
from typing import List
from ..item.base import ItemInterface

class InventoryInterface(ABC):

    @property
    @abstractmethod
    def inventory(self) -> List[ItemInterface]:
        pass

    @property
    @abstractmethod
    def capacity(self) -> int:
        pass

    @abstractmethod
    def add(self, items: List[ItemInterface]) -> None:
        pass

    @abstractmethod
    def remove(self, items: List[ItemInterface]) -> None:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass
