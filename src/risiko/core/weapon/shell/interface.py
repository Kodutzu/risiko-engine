from attrs import define
from abc import ABC, abstractmethod

@define
class ShellInterface(ABC):

    @property
    @abstractmethod
    def damage(self) -> int:
        ...