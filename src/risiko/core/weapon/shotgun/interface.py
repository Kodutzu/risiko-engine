from abc import ABC, abstractmethod
from typing import Union
from ..magazine.interface import MagazineInterface
from ..shell import Shell

class ShotgunInterface(ABC):

    @property
    def magazine(self) -> MagazineInterface:
        ...

    @property
    @abstractmethod
    def chamber(self) -> Union[Shell, None]:
        ...
    
    @property
    @abstractmethod
    def live_damage(self) -> int:
        ...

    @live_damage.setter
    @abstractmethod
    def live_damage(self, value) -> None:
        ...

            