from attrs import define, field
from attrs.validators import instance_of
from random import shuffle
from typing import Literal, Optional, TYPE_CHECKING
from collections import Counter

from ....core.weapon.magazine.interface import MagazineInterface
from ....core.weapon.shell import Shell

if TYPE_CHECKING:
    from .states.interface import MagazineState



@define
class MagazineBehaviour: #Planning to have State Pattern

    _data: MagazineInterface = field(validator=instance_of(MagazineInterface),alias="data")
    _state: "MagazineState" = field(init=False)

    def __attrs_post_init__(self) -> None:

        from .states.empty import EmptyState
        self._state = EmptyState()

    def load_new_round(self, lives: int , blanks: int) -> None:

        self._state.load_round(self, lives, blanks)

    
    def ejection(self) -> Optional[Shell]:
        
        self._state.ejection(self)

    def clear(self) -> None:

        self._state.clear(self)

    def show(self, format: Optional[Literal["deque","counter"]]= "deque") -> None:

        if  format == "deque":
            return self._data.tube
        
        elif format == "counter":
            return Counter(self._data.tube)
        
        else:
            raise ValueError("Invalid format.")
        

    
    def change_state(self, new_state: "MagazineState") -> None:

        self._state = new_state

