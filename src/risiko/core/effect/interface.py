from abc import ABC, abstractmethod

class EffectInterface(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def turn(self) -> int:
        pass

    @property
    @abstractmethod
    def is_active(self) -> bool:
        pass

    @abstractmethod
    def tick(self) -> None:
        pass
