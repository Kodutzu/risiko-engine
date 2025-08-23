from abc import ABC, abstractmethod


class PlayerInterface(ABC):
    @abstractmethod
    def gain_charge(self, amount: int) -> None:
        pass

    @abstractmethod
    def lose_charge(self, amount: int) -> None:
        pass

    @abstractmethod
    def get_charge(self) -> int:
        pass

