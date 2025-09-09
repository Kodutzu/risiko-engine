from abc import ABC, abstractmethod
from enum import Enum

class ItemInterface(ABC):

    @property
    @abstractmethod
    def kind(self) -> Enum:
        ...
    
    @property
    @abstractmethod
    def duration(self) -> int:
        ...

    @abstractmethod
    def radiate(self, amt:int) -> None:
        ...

