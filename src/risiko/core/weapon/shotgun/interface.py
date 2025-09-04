from abc import ABC, abstractmethod
from typing import Optional
from ..magazine.interface import MagazineInterface
from ..shell import Shell

class ShotgunInterface(ABC):

    @property
    def magazine(self) -> MagazineInterface:
        ...

    @property
    @abstractmethod
    def chamber(self) -> Optional[Shell]:
        ...
    
    @chamber.setter
    @abstractmethod
    def chamber(self, shell: Optional[Shell]) -> None:
        ...
    @property
    @abstractmethod
    def live_damage(self) -> int:
        ...

    @live_damage.setter
    @abstractmethod
    def live_damage(self, value: int) -> None:
        ...

            