from .interface import InventoryInterface
from typing import List, override
from attrs  import define, field
from ..item.interface import ItemInterface
from .exceptions import CapacityExceeded, ItemNotFound
from .validator import InventoryValidator

@define
class InventoryBase(InventoryInterface):
    _inventory: List[ItemInterface] = field(factory=list, alias="inventory")
    _capacity: int = field(default=4, validator=InventoryValidator.capacity_check, alias="capacity")
        
    def __attrs_post_init__(self):
   
        if len(self._inventory) > self._capacity:
            raise CapacityExceeded(
                f"Number of items ({len(self._inventory)}) "
                f"cannot exceed capacity ({self._capacity})."
            )
    @property
    def inventory(self) -> List[ItemInterface]:
        return self._inventory
    
    @property
    def capacity(self) -> int:
        return self._capacity

    @override
    def add(self, items: List[ItemInterface]) -> None:
        
        validated_items = InventoryValidator.validate_items(items)

        if len(self._inventory) + len(items) > self._capacity:
            raise CapacityExceeded("Player's Inventory has Reached it's Capacity")
        
        self.inventory.extend(validated_items)

    @override
    def remove(self, items: List[ItemInterface]) -> None:
        
        validated_items = InventoryValidator.validate_items(items)

        for vm in validated_items:
            if vm in self._inventory:
                self._inventory.remove(vm)
            else:
                raise ItemNotFound(f"Item {vm} not found in Inventory")

    @override
    def clear(self) -> None:
        self._inventory.clear()