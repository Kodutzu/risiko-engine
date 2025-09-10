from attrs import define, field
from attrs.validators import instance_of
from random import shuffle
from typing import Literal, Optional, TYPE_CHECKING, Counter, Deque, Union, Type
from collections import Counter

from ....core.weapon.magazine.interface import MagazineInterface
from ....core.weapon.shell.interface import ShellInterface

if TYPE_CHECKING:
    from .states.interface import MagazineState



@define
class MagazineBehaviour:

    _data: MagazineInterface = field(validator=instance_of(MagazineInterface),alias="magazine_base")
    _state: "MagazineState" = field(init=False, repr=False)

    def __attrs_post_init__(self) -> None:

        from .states.empty import EmptyState
        self._state = EmptyState()

    def load_new_round(self, lives: int , blanks: int) -> None:

        self._state.load_round(context=self,lives=lives,blanks=blanks)

    
    def eject_current_shell(self) -> Optional[ShellInterface]:
        try:
            return self._state.ejection(self)
        except Exception: # Catch the exception from EmptyState
            return None

    def clear_shell(self) -> None:

        self._state.clear(context=self)

    def show(self, format: Literal["deque","counter"]= "deque") -> Union[Deque[ShellInterface], Counter[ShellInterface]]:
        if  format == "deque":
            return self._data.tube
        
        elif format == "counter":
            return Counter(self._data.tube)
        
        else:
            raise ValueError("Invalid format.")
        

    
    def _change_state(self, new_state: "MagazineState") -> None:

        self._state = new_state

