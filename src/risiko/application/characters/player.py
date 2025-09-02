from attrs import define, field

from ...core.player.base import PlayerBase
from ...core.player.interface import PlayerInterface


@define
class PlayerCharacter:

    data: PlayerInterface = field(factory=PlayerBase, alias="data")
    # _state: PlayerState = field(factory=PlayerState)


    def can_perform_action(self) -> bool:
        ...

    def change_state(self, new_state) -> None:
        ...

    
