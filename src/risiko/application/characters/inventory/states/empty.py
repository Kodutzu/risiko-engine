from typing import TYPE_CHECKING, List, NoReturn, Union, override


from .....core.item.interface import ItemInterface
from .....core.inventory.exceptions import CapacityExceeded, ItemNotFound
from .interface import InventoryState
from ..validator import InventoryValidator


if TYPE_CHECKING:
    from ..behaviour import InventoryBehaviour

class EmptyState(InventoryState):

    @override
    def add(self, context: "InventoryBehaviour", items: List[ItemInterface]) -> Union[None, NoReturn]:
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

    @override
    def remove(self, context: "InventoryBehaviour", items: List[ItemInterface]) -> NoReturn:

        raise ItemNotFound("Cannot remove items: inventory is empty.")
    
    @override
    def clear(self, context: "InventoryBehaviour") -> NoReturn:

        raise ItemNotFound("Cannot clear items: inventory is already empty.")
    

