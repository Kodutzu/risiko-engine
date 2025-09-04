from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, List, Optional
from .....core.item.interface import ItemInterface

if TYPE_CHECKING:
    from ..behaviour import InventoryBehaviour


class InventoryState(ABC):

    @abstractmethod
    def add(self, context: "InventoryBehaviour", items: List[ItemInterface]) -> Optional[None] :

        pass

    @abstractmethod
    def remove(self, context: "InventoryBehaviour", items: List[ItemInterface]) -> Optional[None]:
        pass

    @abstractmethod
    def clear(self, context: "InventoryBehaviour") -> Optional[None]:
        pass
