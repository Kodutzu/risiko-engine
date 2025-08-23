from abc import ABC, abstractmethod

class EffectorInterface(ABC):
    @abstractmethod
    def add(self, target):
        pass

    @abstractmethod
    def remove(self, target):
        pass

    @abstractmethod
    def remove_expired(self) -> bool:
        pass

    @abstractmethod
    def tick_all(self) -> None:
        pass
