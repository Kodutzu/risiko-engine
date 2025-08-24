from ...constants.shell import Shell
from .interface import MagazineInterface
from .validator import bullet_number_checker
from attrs import define, field, setters
from typing import Deque, Union, override, overload, Literal
from collections import deque, Counter
from .exceptions import MagazineException
import random 

@define
class MagazineBase(MagazineInterface):

    tube: Deque[Shell] = field(factory=deque)
    lives: int = field(default=4,validator=bullet_number_checker, on_setattr=setters.frozen)
    blanks: int = field(default=4, validator=bullet_number_checker,on_setattr=setters.frozen)

    def __attrs_post_init__(self):

        if self.is_tube_empty:
            self.tube = deque([Shell.LIVE] * self.lives + [Shell.BLANK] * self.blanks)
            self.reload()
    
    @property
    @override
    def has_mixed_bullets(self) -> bool:

        return (Shell.LIVE in self.tube) and (Shell.BLANK in self.tube)
    
    @property
    @override
    def is_tube_empty(self) -> bool:

        return not self.tube

    @override
    def reload(self) -> None:

        random.shuffle(self.tube)

    @overload
    def show(self, as_deque:bool= Literal[True]) -> Deque[Shell]: 
        pass

    @overload
    def show(self, as_deque: bool = Literal[False]) -> Counter[Shell, int]:
        pass
    
    def show(self, as_deque: bool=True) -> Union[Deque[Shell], Counter[Shell, int]]:

        if as_deque :
            return self.tube
        else:
            return Counter(self.tube)

    @override 
    def take_out_bullet(self) -> Shell:
        
                
        if self.is_tube_empty:
            raise MagazineException("Reload: Magazine is empty.")
        
        if not self.has_mixed_bullets:
            raise MagazineException("Reload: Magazine does not have a mix of live and blank shells.")

        return self.tube.popleft()
    
