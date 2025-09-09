from abc import ABC, abstractmethod
from typing import Deque
from ..shell.interface import ShellInterface


class MagazineInterface(ABC):

    @property
    @abstractmethod
    def tube(self) ->  Deque[ShellInterface]:
        ...
    
    @property
    @abstractmethod
    def is_tube_empty(self) ->  bool:
        ...

    @property
    @abstractmethod
    def has_mixed_bullets(self) ->  bool:
        ...
