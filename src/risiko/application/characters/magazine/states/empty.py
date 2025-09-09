from .interface import MagazineState
from typing import TYPE_CHECKING, NoReturn, override
from .....core.weapon.shell.interface import ShellInterface
from .....core.weapon.shell.live import LiveShell
from .....core.weapon.shell.blank import BlankShell
from random import shuffle

if TYPE_CHECKING:
    from ..behaviour import MagazineBehaviour


class EmptyState(MagazineState):

    @override
    def load_round(self, context: "MagazineBehaviour" ,lives:int, blanks:int) -> None:

        shells = [LiveShell() for _ in range(lives)] + [BlankShell() for _ in range(blanks)]
        shuffle(shells)
        context._data.tube.extend(shells)

        from .stocked import StockedState
        context._change_state(StockedState())

    @override
    def ejection(self, context: "MagazineBehaviour") -> NoReturn:
        
        raise Exception("Magazine is Empty")

    @override
    def clear(self, context: "MagazineBehaviour") -> NoReturn :

        raise Exception("Magazine is already Empty")
        
