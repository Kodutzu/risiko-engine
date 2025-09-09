from .interface import MagazineState
from typing import TYPE_CHECKING, NoReturn, override
from .....core.weapon.shell import Shell 
from random import shuffle

if TYPE_CHECKING:
    from ..behaviour import MagazineBehaviour


class EmptyState(MagazineState):

    @override
    def load_round(self, context: "MagazineBehaviour" ,lives:int, blanks:int) -> None:

        context._data.tube.extend( ([Shell.LIVE] * lives) + ([Shell.BLANK] * blanks) )
        shuffle(context._data.tube)

        from .stocked import StockedState
        context._change_state(StockedState())

    @override
    def ejection(self, context: "MagazineBehaviour") -> NoReturn:
        
        raise Exception("Magazine is Empty")

    @override
    def clear(self, context: "MagazineBehaviour") -> NoReturn :

        raise Exception("Magazine is already Empty")
        
