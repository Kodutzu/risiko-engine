from attrs import define, field, Factory
from attrs.validators import instance_of
from typing import Deque, override, final
from collections import deque

from ..shell import Shell
from .interface import MagazineInterface


@define
class MagazineBase(MagazineInterface):

    _tube: Deque[Shell] = field(default=Factory(deque), alias="tube", validator=instance_of(deque))
    
    def __attrs_post_init__(self):

        if self._tube: #If Tube is not empty, then Validate
             if not all(isinstance(shell, Shell) for shell in self._tube):
                 raise ValueError("All elements in 'tube' must be instances of Shell.")
            

    @property
    @override
    @final
    def tube(self) -> Deque[Shell]:
    
            return self._tube

    @property
    @override
    @final
    def is_tube_empty(self) -> bool:

        return not self._tube
    
    @property
    @override
    @final
    def has_mixed_bullets(self) -> bool:

        return (Shell.LIVE in self._tube) and (Shell.BLANK in self._tube)

