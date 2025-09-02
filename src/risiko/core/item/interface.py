from abc import ABC, abstractmethod
from enum import Enum

class ItemInterface(ABC):

    @property
    @abstractmethod
    def entity(self) -> Enum:
        ...
