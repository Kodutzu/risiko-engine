from abc import ABC, abstractmethod
from typing import List, Union
from ...constants.shell import Shell

class MagazineInterface(ABC):

    @abstractmethod
    def reload(self) -> None:
        pass

    @abstractmethod
    def show(self, as_deque: bool =True) -> Union[List[Shell], dict]:
        pass

    @abstractmethod
    def has_mixed_bullets(self) -> bool:
        pass
        
    @abstractmethod
    def take_out_bullet(self) -> Shell:
        pass

class ShotgunInterface(ABC):

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
            
    @abstractmethod
    def set_live_damage(self,new_dmg) -> None:
        pass