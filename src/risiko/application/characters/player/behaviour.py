from attrs import define, field, setters, Factory
from attrs.validators import instance_of
from typing import TYPE_CHECKING

from ....core.player.interface import PlayerInterface

if TYPE_CHECKING:
    from .states.interface import PlayerState



@define
class PlayerBehaviour:

    _data: PlayerInterface = field(validator=instance_of(PlayerInterface), alias="player_base")
    _state: "PlayerState" = field(init=False, repr=False)

    def __attrs_post_init__(self):

        from .states.alive import AliveState
        self._state = AliveState()
    
    @property
    def id(self) -> str:
        return self._data.id

    def lose_charges(self, amt: int) -> None:
        try:
            self._state.lose_charges(context=self, amt= amt)
        except Exception: # Catch the exception from DeadState
            pass # Do nothing, charges should not change when dead


    def gain_charges(self, amt: int) -> None:
        try:
            self._state.gain_charges(context=self, amt=amt)
        except Exception: # Catch the exception from DeadState
            pass # Do nothing, charges should not change when dead
        

    def change_state(self, new_state: "PlayerState") -> None:

        self._state = new_state
