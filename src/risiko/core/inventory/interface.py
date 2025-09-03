from abc import ABC , abstractmethod
from typing import List
from ..item.interface import ItemInterface


class InventoryInterface(ABC):

    @property
    @abstractmethod
    def inventory(self) -> List[ItemInterface]:
        ...

    @property
    @abstractmethod
    def capacity(self) -> int:
        ...

