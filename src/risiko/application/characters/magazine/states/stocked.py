from .interface import MagazineState
from typing import TYPE_CHECKING, NoReturn, Union, NoReturn,override
from .....core.weapon.shell.interface import ShellInterface

if TYPE_CHECKING:
    from ..behaviour import MagazineBehaviour


class StockedState(MagazineState):

    @override
    def load_round(self, context: "MagazineBehaviour",lives=int, blanks=int) -> NoReturn:

        raise Exception("Magazine is already stocked.")


    @override
    def ejection(self, context: "MagazineBehaviour") -> ShellInterface:

        shell = context._data.tube.popleft()

        if context._data.is_tube_empty:
            from .empty import EmptyState
            context._change_state(EmptyState())

        return shell
    
    @override
    def clear(self, context: "MagazineBehaviour") -> None :

        context._data.tube.clear()

        from .empty import EmptyState
        context._change_state(EmptyState())
        