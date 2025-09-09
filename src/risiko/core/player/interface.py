from abc import ABC, abstractmethod

class PlayerInterface(ABC):

    @property
    @abstractmethod
    def id(self) -> str: ...

    @property
    @abstractmethod
    def charges(self) -> int:...

    @charges.setter
    @abstractmethod
    def charges(self, value: int) -> None: ...



