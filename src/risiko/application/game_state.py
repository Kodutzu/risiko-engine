#contains the live snapshot of the game, which is updated after every turn
#Will be using Pydantic to build it!
#It will contains methods such as to_snapshot, change_transition and many more!
from pydantic import BaseModel, Field
from collections import deque
from typing import Dict

from .characters.player.behaviour import PlayerBehaviour
from .characters.shotgun.behaviour import ShotgunBehaviour
from .flow.interface import GameFlowState


class GameState(BaseModel):
    state: GameFlowState = Field(init=False)
    shotgun: ShotgunBehaviour = Field(init=False)
    players: Dict[int,PlayerBehaviour] = Field(init=False)
    #turns: TurnManager = Field(init=False)
    #rounds: RoundManager = Field(init=False)
