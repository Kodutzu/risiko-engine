from attrs import define, field,Factory, setters
from attrs.validators import instance_of
from typing import Deque, final, Final, Type
from collections import deque

from ..shell.interface import ShellInterface
from ..shell.live import LiveShell 
from ..shell.blank import BlankShell


@define
class MagazineBase:
     
    tube: Final[Deque[ShellInterface]] = field(default=Factory(deque), validator=instance_of(deque), on_setattr=setters.frozen)

    @property
    @final
    def is_tube_empty(self) -> bool:

        return not self.tube
    
    @property
    @final
    def has_mixed_bullets(self) -> bool:

        has_live = any(isinstance(shell, LiveShell) for shell in self.tube) 
        has_blank = any(isinstance(shell, BlankShell) for shell in self.tube)
        
        return has_live and has_blank

    
