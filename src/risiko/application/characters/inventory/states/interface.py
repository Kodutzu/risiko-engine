from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, List
from .....core.item.interface import ItemInterface

if TYPE_CHECKING:
    from ..behaviour import InventoryBehaviour


class InventoryState(ABC):

    @abstractmethod
    def add(self, context: "InventoryBehaviour", items: List[ItemInterface]):

        pass

    @abstractmethod
    def remove(self, context: "InventoryBehaviour", items: List[ItemInterface]):
        pass

    @abstractmethod
    def clear(self, state: "InventoryBehaviour"):
        pass
