from attrs import define, field
from attrs.validators import instance_of
from typing import Deque, Optional, override
from collections import deque

from ..shell import Shell
from .interface import MagazineInterface


@define
class MagazineBase(MagazineInterface):

    _tube: Optional[Deque[Shell]] = field(factory=deque, alias="tube", validator=instance_of(deque))
    
        
    @property
    @override
    def tube(self) -> Deque[Shell]:
    
            return self._tube

    @property
    @override
    def is_tube_empty(self) -> bool:

        return not self._tube
    
    @property
    @override
    def has_mixed_bullets(self) -> bool:

        return (Shell.LIVE in self._tube) and (Shell.BLANK in self._tube)

