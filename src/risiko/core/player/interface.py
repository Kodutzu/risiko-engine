from abc import ABC, abstractmethod


class PlayerInterface(ABC):

    @property
    @abstractmethod
    def id(self) -> str:
        pass
    
    @property
    @abstractmethod
    def charges(self) -> int:
        pass

    @abstractmethod
    def gain_charge(self, amt: int) -> None:
        pass

    @abstractmethod
    def lose_charge(self, amt: int) -> None:
        pass



