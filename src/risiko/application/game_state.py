#contains the live snapshot of the game, which is updated after every turn
#Will be using Pydantic to build it!
#It will contains methods such as to_snapshot, change_transition and many more!
from pydantic import BaseModel, Field

from .managers.turn import TurnManager
from .managers.round import RoundManager
from .managers.player import PlayerManager
from .managers.weapon import WeaponManager
from .flow.interface import FlowInterface


class GameState(BaseModel):

    _flow: FlowInterface = Field(init=False)
    player: PlayerManager = Field(init=False)
    turns: TurnManager = Field(init=False)
    rounds: RoundManager = Field(init=False)
    weapons: WeaponManager = Field(init=False)

