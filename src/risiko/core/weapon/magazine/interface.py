from abc import ABC, abstractmethod
from typing import Deque
from ..shell import Shell


class MagazineInterface(ABC):

    
    @property
    @abstractmethod
    def tube(self) ->  Deque[Shell]:
        
        pass
    
    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def take_out_bullet(self) -> Shell:
        pass