from attrs import define, field,setters, evolve
from attrs.validators import instance_of
from typing import Deque, final, Tuple
from collections import deque
from random import shuffle

from ..shell.interface import ShellInterface
from ..shell.live import LiveShell 
from ..shell.blank import BlankShell

@define(frozen=True)
class MagazineBase:
     
    tube: Deque[ShellInterface] = field(factory=deque, validator=instance_of(deque), on_setattr=setters.frozen)

    @property
    @final
    def is_empty(self) -> bool:

        return not self.tube


    def load_round(self,lives:int, blanks:int) -> "MagazineBase":

        new_tube = self.tube.copy()
        shells = [LiveShell()]* lives + [BlankShell()]* blanks
        shuffle(shells)

        new_tube.extend(shells)

        return evolve(self, tube=new_tube)
    
    def eject_shell(self) -> Tuple[ShellInterface, "MagazineBase"]:

        if self.is_empty:
            raise Exception("Magazine is Empty")

        new_tube = self.tube.copy()

        shell = new_tube.popleft()
            
        return (shell, evolve(self, tube=new_tube))
    
    def clear(self) -> "MagazineBase":

        if self.is_empty:
            
            raise Exception("Magazine is already Empty")

        new_tube = self.tube.copy()
        new_tube.clear()

        return evolve(self, tube=new_tube)


     


    
