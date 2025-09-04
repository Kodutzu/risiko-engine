from .interface import MagazineState
from typing import TYPE_CHECKING, NoReturn, Union
from .....core.weapon.shell import Shell 

if TYPE_CHECKING:
    from ..behaviour import MagazineBehaviour


class StockedState(MagazineState):

    def load_round(self, context: "MagazineBehaviour",lives=int, blanks=int) -> NoReturn:

        raise Exception("Magazine is already stocked.")


    def ejection(self, context: "MagazineBehaviour") -> Union[Shell, None]:

        shell = context._data.tube.popleft()

        if context._data.is_tube_empty:
            from .empty import EmptyState
            context.change_state(EmptyState())

        else: 
            #remain in Stocked State and Return Shell
            return shell
    
    
    def clear(self, context: "MagazineBehaviour") -> None :

        context._data.tube.clear()

        from .empty import EmptyState
        context.change_state(EmptyState())
        