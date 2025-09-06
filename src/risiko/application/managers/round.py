from typing import Deque
from collections import deque
from attrs import define, field, Factory
from attrs.validators import instance_of, ge

from ..characters.shotgun.behaviour import ShotgunBehaviour 
from ..characters.player.behaviour import PlayerBehaviour

@define
class RoundManager:
  
    _round_number: int = field(default=0, validator=ge(0), init=False)
    _player_behaviour: PlayerBehaviour = field(validator=instance_of(PlayerBehaviour) )
    _shotgun_behaviour: ShotgunBehaviour = field(validator=instance_of(ShotgunBehaviour))


    @property
    def round_number(self) -> int:
        
        return self._round_number

    def start_round(self):
     
        self._round_number += 1
        # refill inventory with ITem, and start a new round.

    def end_round(self): ...


    def is_round_over(self):
        pass
        # It asks the expert for the information it needs to make a decision.
        