from attrs import define, field
from random import shuffle
from typing import Literal, Optional
from collections import Counter

from ....core.weapon.magazine.base import MagazineBase
from ....core.weapon.magazine.interface import MagazineInterface
from ....core.weapon.shell import Shell


@define
class MagazineBehaviour:

    _data: MagazineInterface = field(alias="magazine")

    def load_new_round(self, lives: int, blanks: int):

        self._data.tube.clear()
        self._data.tube.extend( ([Shell.LIVE] * lives) + ([Shell.BLANK] * blanks) )
        shuffle(self._data.tube)

    def show(self, format: Optional[Literal["deque","counter"]]= "deque") -> None:

        if  format == "deque":
            return self._data.tube
        
        elif format == "counter":
            return Counter(self._data.tube)
        

    def take_out_bullet(self) -> Shell:
        
                
        if self._data.is_tube_empty:
            raise Exception("Reload: Magazine is empty.")
        
        if not self._data.has_mixed_bullets:
            raise Exception("Reload: Magazine does not have a mix of live and blank shells.")

        return self._data.tube.popleft()