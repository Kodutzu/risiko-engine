from .interface import MagazineState
from typing import TYPE_CHECKING, NoReturn, override

if TYPE_CHECKING:
    from ..behaviour import MagazineBehaviour


class JammedState(MagazineState):

    @override
    def load_round(self, context: "MagazineBehaviour",lives=int, blanks=int) -> NoReturn:

        raise Exception("Clear the Magazine before loading a new round.")


    @override
    def ejection(self, context: "MagazineBehaviour") -> NoReturn:
        
        raise Exception("Magazine is Jammed, cannot eject.")

    
    @override
    def clear(self, context: "MagazineBehaviour") -> None :

        context._data.tube.clear()

        from .empty import EmptyState
        context._change_state(EmptyState())
        
