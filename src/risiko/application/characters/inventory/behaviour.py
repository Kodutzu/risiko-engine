from typing import List, TYPE_CHECKING
from attrs import define, field
from attrs.validators import instance_of

from ....core.inventory.interface import InventoryInterface
from ....core.item.interface import ItemInterface
from ....core.item.item_type import ItemType

if TYPE_CHECKING:
    from .states.interface import InventoryState


@define
class InventoryBehaviour:
        
    _data: InventoryInterface = field(validator=instance_of(InventoryInterface),alias="data")
    _state: "InventoryState" = field(init=False, repr=False)

    def __attrs_post_init__(self):

        from .states.empty import EmptyState

        self._state = EmptyState()

    #New change - Inventory will Depend on ItemEffect
    def add(self, items: List[ItemInterface]) -> None:

        self._state.add(self, items)
        

    def remove(self, items: List[ItemInterface]) -> None:
        
        self._state.remove(self, items)

    def has(self, item: ItemInterface ) -> bool:

        return item in self._data.inventory
    
    def show(self) -> List[ItemInterface]:

        return self._data.inventory

    def clear(self) -> None:

        self._state.clear(self)

    def change_state(self, new_state: "InventoryState") -> None:

        self._state = new_state

