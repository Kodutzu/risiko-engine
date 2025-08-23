from abc import ABC, abstractmethod
from typing import List
from ..item.base import Item

class InventoryInterface(ABC):
    @abstractmethod
    def add(self, items: List[Item]) -> None:
        pass

    @abstractmethod
    def remove(self, items: List[Item]) -> None:
        pass

    @abstractmethod
    def show(self) -> List[Item]:
        pass

    @abstractmethod
    def has(self, item: Item) -> bool:
        pass

    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def space(self) -> int: 
        pass

    @abstractmethod
    def clear(self) -> None:
        pass
    
