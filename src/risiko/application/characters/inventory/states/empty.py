from typing import TYPE_CHECKING, List


from .....core.item.interface import ItemInterface
from .....core.inventory.exceptions import CapacityExceeded, ItemNotFound
from .interface import InventoryState
from ..validator import InventoryValidator


if TYPE_CHECKING:
    from ..behaviour import InventoryBehaviour
    from .available import AvailableState
    from .full import FullState

class EmptyState(InventoryState):

    def add(self, context: "InventoryBehaviour", items: List[ItemInterface]):
        from .available import AvailableState
        from .full import FullState
 
        validated_items = InventoryValidator.validate_items(items)
        if len(validated_items) > context._data.capacity:
            raise CapacityExceeded("Cannot add items: inventory capacity reached.")
        
        context._data.inventory.extend(validated_items)

        if len(context._data.inventory) == context._data.capacity:
            context.change_state(FullState())
        else:
            context.change_state(AvailableState())

    def remove(self, context: "InventoryBehaviour", items: List[ItemInterface]):

        raise ItemNotFound("Cannot remove items: inventory is empty.")
    
    def clear(self, context: "InventoryBehaviour") -> None:

        raise ItemNotFound("Cannot clear items: inventory is already empty.")
    

