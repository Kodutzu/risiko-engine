from .interface import PlayerState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..behaviour import PlayerBehaviour


class AliveState(PlayerState):


    
    def lose_charges(self, context: "PlayerBehaviour", amt: int) -> None:

        context._data.charges -= amt

        if context._data.charges <= 0:
            from .dead import DeadState
            context.change_state(DeadState())

    def gain_charges(self, context: "PlayerBehaviour", amt: int) -> None:
        
        context._data.charges +=amt
        


