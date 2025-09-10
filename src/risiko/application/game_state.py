#contains the live snapshot of the game, which is updated after every turn
#Will be using Pydantic to build it!
#It will contains methods such as to_snapshot, change_transition and many more!
from attrs import define, field

from .managers.turn import TurnManager
from .managers.round import RoundManager
from .managers.player import PlayerManager
from .managers.weapon import WeaponManager
from .flow.interface import FlowInterface

@define
class GameState:

    _flow: FlowInterface 
    player: PlayerManager 
    turns: TurnManager 
    rounds: RoundManager 
    weapons: WeaponManager 



    

