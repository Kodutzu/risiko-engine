from abc import ABC, abstractmethod
from typing import Optional
from ..magazine.interface import MagazineInterface
from ..shell.interface import ShellInterface

class ShotgunInterface(ABC):

    @property
    @abstractmethod
    def id(self) -> str:
        ...
    @property
    @abstractmethod
    def magazine(self) -> MagazineInterface:
        ...

    @property
    @abstractmethod
    def chamber(self) -> Optional[ShellInterface]:
        ...
    
    @chamber.setter
    @abstractmethod
    def chamber(self, shell: Optional[ShellInterface]) -> None:
        ...


            