from abc import ABC, abstractmethod
from typing import Deque
from ..shell import Shell


class MagazineInterface(ABC):

    @property
    @abstractmethod
    def tube(self) ->  Deque[Shell]:
        ...
    
    @property
    @abstractmethod
    def is_tube_empty(self) ->  bool:
        ...

    @property
    @abstractmethod
    def has_mixed_bullets(self) ->  bool:
        ...
