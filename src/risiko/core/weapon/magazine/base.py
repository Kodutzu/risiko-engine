from attrs import define, field
from typing import Deque, Optional, override
from collections import deque

from ..shell import Shell
from .interface import MagazineInterface


@define
class MagazineBase(MagazineInterface):

    _tube: Optional[Deque[Shell]] = field(factory=deque, alias="tube")
    
        
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

