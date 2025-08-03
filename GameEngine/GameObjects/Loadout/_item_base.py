
from abc import ABC, abstractmethod
from dataclasses import dataclass
from ...GameException.item_exception import ItemException
@dataclass
class _ItemBase(ABC):
    """
    A base class for all item data models.
    Items should be simple data containers with no game logic.
    """
    # The __str__ method is still useful for printing item names
    def __str__(self):
        return self.__class__.__name__

