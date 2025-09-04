from typing import TYPE_CHECKING, List, Union, NoReturn, override


from .....core.item.interface import ItemInterface
from .....core.inventory.exceptions import CapacityExceeded, ItemNotFound, InvalidItem, InvalidList
from .interface import InventoryState
from ..validator import InventoryValidator

if TYPE_CHECKING:
    from ..behaviour import InventoryBehaviour



class AvailableState(InventoryState):

    @override
    def add(self, context: "InventoryBehaviour", items: List[ItemInterface]) -> Union[None, NoReturn]:


        validated_items = InventoryValidator.validate_items(items)
        if len(context._data.inventory) + len(validated_items) > context._data.capacity:
            raise CapacityExceeded("Cannot add items: inventory capacity reached.")

        context._data.inventory.extend(validated_items)

        # After adding, check if we need to transition to the Full state.
        if len(context._data.inventory) == context._data.capacity:

            from .full import FullState
            context.change_state(FullState())
            

    @override
    def remove(self, context: "InventoryBehaviour", items: List[ItemInterface]) -> Union[None, NoReturn]:
 
        
        validated_items = InventoryValidator.validate_items(items)

        for item in validated_items:

            try: # this has logical error - If there's one Item A, and If I ordered to remove [Item A, Item A] - then it will fail critically
                context._data.inventory.remove(item)

            except ValueError:
                raise ItemNotFound(f"Cannot remove: {item.kind.name} not found.")

        # After removing, check if we need to transition to the Empty state.
        if not context._data.inventory:
            from .empty import EmptyState
            context.change_state(EmptyState())


    @override
    def clear(self, context: "InventoryBehaviour") -> None:
        from .empty import EmptyState

        context._data.inventory.clear()
        context.change_state(EmptyState())