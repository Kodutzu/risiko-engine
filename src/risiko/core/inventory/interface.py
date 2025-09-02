from abc import ABC , abstractmethod
from typing import List
from ..item.interface import ItemInterface


class InventoryInterface(ABC):

    @property
    def inventory(self) -> List[ItemInterface]:
        ...

    @property
    def capacity(self) -> int:
        ...

