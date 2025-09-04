from typing import TYPE_CHECKING, List, NoReturn, Union


from .....core.item.interface import ItemInterface
from .....core.inventory.exceptions import CapacityExceeded, ItemNotFound
from .interface import InventoryState
from ..validator import InventoryValidator


if TYPE_CHECKING:
    from ..behaviour import InventoryBehaviour




class FullState(InventoryState):

    def add(self, context: "InventoryBehaviour", items: List[ItemInterface]) -> NoReturn:
    
        raise CapacityExceeded(f"Cannot add items: inventory is full")

    def remove(self, context: "InventoryBehaviour", items: List[ItemInterface]) -> Union[None, NoReturn]:


        validated_items = InventoryValidator.validate_items(items)
        for item in validated_items:
            try:
                context._data.inventory.remove(item)
            except ValueError:
                raise ItemNotFound(f"Cannot remove: {item.kind.name} not found.")

        from .available import AvailableState
        context.change_state(AvailableState())

    def clear(self, context: "InventoryBehaviour") -> None:
   

        context._data.inventory.clear()

        from .empty import EmptyState
        context.change_state(EmptyState())