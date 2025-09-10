from .interface import PlayerState
from typing import TYPE_CHECKING, override

if TYPE_CHECKING:
    from ..behaviour import PlayerBehaviour


class AliveState(PlayerState):


    @override
    def lose_charges(self, context: "PlayerBehaviour", amt: int) -> None:

        context._data.charges = max(0, context._data.charges - amt)

        if context._data.charges <= 0:
            from .dead import DeadState
            context.change_state(DeadState())

    @override
    def gain_charges(self, context: "PlayerBehaviour", amt: int) -> None:
        
        context._data.charges +=amt
        


