from abc import ABC, abstractmethod
from typing import Union
from ..magazine.interface import MagazineInterface
from ..shell import Shell

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

    @live_damage.setter
    @abstractmethod
    def live_damage(self, value) -> None:
        pass

            