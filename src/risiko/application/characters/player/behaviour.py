from attrs import define, field

from ....core.player.base import PlayerBase
from ....core.player.interface import PlayerInterface
from ..inventory.behaviour import InventoryBehaviour


@define
class PlayerBehaviour:

    data: PlayerInterface = field( alias="data")
    inventory: InventoryBehaviour = field(alias="inventory")
    # _state: PlayerState = field(factory=PlayerState)


    def can_perform_action(self) -> bool:
        ...

    def change_state(self, new_state) -> None:
        ...

    
