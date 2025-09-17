from attrs import define, field
from .managers import PlayerManager, TurnManager
from ..core.shotgun import ShotgunBase, ShotgunInterface


@define(frozen=True)
class RisikoState:
    """Represents the live snapshot of the game state.
    This class is immutable; any updates to the game state will result in a new RisikoState instance.
    """

    player: PlayerManager = field(factory=PlayerManager)
    turns: TurnManager  = field(factory=TurnManager)
    shotgun: ShotgunInterface = field(factory=ShotgunBase)
    


  



    

