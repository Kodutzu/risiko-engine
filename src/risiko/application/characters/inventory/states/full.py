from typing import TYPE_CHECKING, List


from .....core.item.interface import ItemInterface
from .....core.inventory.exceptions import CapacityExceeded, ItemNotFound
from .interface import InventoryState
from ..validator import InventoryValidator


if TYPE_CHECKING:
    from ..behaviour import InventoryBehaviour
    from .available import AvailableState
    from .empty import EmptyState



class FullState(InventoryState):

    def add(self, context: "InventoryBehaviour", items: List[ItemInterface]):
    
        raise CapacityExceeded(f"Cannot add items: inventory is full")

    def remove(self, context: "InventoryBehaviour", items: List[ItemInterface]):
        from .available import AvailableState

        validated_items = InventoryValidator.validate_items(items)
        for item in validated_items:
            try:
                context._data.inventory.remove(item)
            except ValueError:
                raise ItemNotFound(f"Cannot remove: {item.entity.name} not found.")

        context.change_state(AvailableState())

    def clear(self, context: "InventoryBehaviour") -> None:
        from .empty import EmptyState

        context._data.inventory.clear()
        context.change_state(EmptyState())