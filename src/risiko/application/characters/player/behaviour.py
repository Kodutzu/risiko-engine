from attrs import define, field, setters, Factory
from attrs.validators import instance_of
from typing import Optional, TYPE_CHECKING

from ....core.player.interface import PlayerInterface
from ..shotgun.behaviour import ShotgunBehaviour

if TYPE_CHECKING:
    from .states.interface import PlayerState



@define
class PlayerBehaviour:

    _data: PlayerInterface = field(validator=instance_of(PlayerInterface), alias="data")
    _state: "PlayerState" = field(init=False, repr=False)

    def __attrs_post_init__(self):

        from .states.alive import AliveState
        self._state = AliveState()
    
    @property
    def id(self) -> str:
        return self._data.id
    
    def shoot(self,gun: ShotgunBehaviour) -> Optional[None]:
        
        return gun.fire()

    def lose_charges(self, amt: int) -> None:
        self._state.lose_charges(context=self, amt= amt)


    def gain_charges(self, amt: int) -> None:
        self._state.gain_charges(context=self, amt=amt)
        

    def change_state(self, new_state: "PlayerState") -> None:

        self._state = new_state
