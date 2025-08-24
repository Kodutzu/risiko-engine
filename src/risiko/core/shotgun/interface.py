from abc import ABC, abstractmethod
from typing import List, Union, Deque
from ...constants.shell import Shell

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

class ShotgunInterface(ABC):

    @property
    def magazine(self) -> MagazineInterface:
        pass

    @property
    @abstractmethod
    def chamber(self) -> Union[Shell, None]:
        pass
    
    @property
    @abstractmethod
    def live_damage(self) -> int:
        pass

    @abstractmethod
    def load_chamber(self) -> Shell:
        pass
            