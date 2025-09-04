from .interface import PlayerState
from typing import TYPE_CHECKING, NoReturn

if TYPE_CHECKING:
    from ..behaviour import PlayerBehaviour


class DeadState(PlayerState):


    
    def lose_charges(self, context: "PlayerBehaviour", amt: int) -> NoReturn:

        raise Exception("Player is already Dead, you can't lose charges")

    def gain_charges(self, context: "PlayerBehaviour", amt: int) -> NoReturn:
        
        raise Exception("Player is Dead - You can't gain charges")
        

