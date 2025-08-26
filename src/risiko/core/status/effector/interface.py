from abc import ABC, abstractmethod

class EffectorInterface(ABC):


    @property
    @abstractmethod
    def effector(self) :
        pass

    @abstractmethod
    def add(self, target) -> None:
        pass

    @abstractmethod
    def remove(self, target) -> None:
        pass

    @abstractmethod
    def remove_expired(self) :
        pass

    @abstractmethod
    def reduce_all(self) -> None:
        pass
