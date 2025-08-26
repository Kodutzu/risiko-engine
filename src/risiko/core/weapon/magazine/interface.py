from abc import ABC, abstractmethod
from ..shell import Shell

class MagazineInterface(ABC):

    @abstractmethod
    def reload(self) -> None:
        pass

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def take_out_bullet(self) -> Shell:
        pass