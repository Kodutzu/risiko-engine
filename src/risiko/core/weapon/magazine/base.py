from attrs import define, field, setters
from typing import Deque, Union, override, overload, Literal
from collections import deque, Counter
import random 

from ..shell import Shell
from .interface import MagazineInterface
from .validator import bullet_number_checker


@define
class MagazineBase(MagazineInterface):

    _tube: Deque[Shell] = field(factory=deque)
    
    @property
    @override
    def is_tube_empty(self) -> bool:

        return not self.tube
    
    @overload
    def show(self, as_deque: bool = Literal[True]) -> Deque[Shell]: 
        pass

    @overload
    def show(self, as_deque: bool = Literal[False]) -> Counter[Shell, int]:
        pass
    
    def show(self, as_deque: bool=True) -> Union[Deque[Shell], Counter[Shell, int]]:

        if as_deque :
            return self.tube
        else:
            return Counter(self.tube)


    
