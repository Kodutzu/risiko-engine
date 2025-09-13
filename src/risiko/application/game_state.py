#contains the live snapshot of the game, which is updated after every turn
#Will be using Pydantic to build it!
#It will contains methods such as to_snapshot, change_transition and many more!
from attrs import define, field

from .managers.turn import TurnManager
from .managers.player import PlayerManager
from ..core.shotgun.interface import ShotgunInterface
from ..core.shotgun.base import ShotgunBase


@define(frozen=True)
class GameState:

    player: PlayerManager = field(factory=PlayerManager)
    turns: TurnManager  = field(factory=TurnManager)
    shotgun: ShotgunInterface = field(factory=ShotgunBase)


  



    

