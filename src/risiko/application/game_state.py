#contains the live snapshot of the game, which is updated after every turn
#Will be using Pydantic to build it!
#It will contains methods such as to_snapshot, change_transition and many more!
from pydantic import BaseModel, Field

from .managers.turn import TurnManager
from .managers.round import RoundManager
from .managers.player import PlayerManager
from .managers.effect import EffectManager
from .managers.item import ItemManager
from .managers.weapon import WeaponManager
from .flow.interface import GameFlowState





class GameState(BaseModel):
    flow: GameFlowState = Field(init=False)
    player: PlayerManager = Field(init=False)
    turns: TurnManager = Field(init=False)
    rounds: RoundManager = Field(init=False)
    effects: EffectManager = Field(init=False)
    items: ItemManager = Field(init=False)
    weapons: WeaponManager = Field(init=False)

