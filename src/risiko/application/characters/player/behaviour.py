from attrs import define, field
from attrs.validators import instance_of
from ....core.player.interface import PlayerInterface
from ..inventory.behaviour import InventoryBehaviour


@define
class PlayerBehaviour:

    data: PlayerInterface = field(validator=instance_of(PlayerInterface), alias="data")
    inventory: InventoryBehaviour = field(validator=instance_of(InventoryBehaviour),alias="inventory")
    # _state: PlayerState = field(factory=PlayerState)


    def can_perform_action(self) -> bool:
        ...

    def change_state(self, new_state) -> None:
        ...

    
