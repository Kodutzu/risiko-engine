from .interface import InventoryInterface
from typing import List, override
from attrs  import define, field
from ..item.base import ItemBase
from .exceptions import CapcityExceeded, ItemNotFound
from .validator import InventoryValidator, capacity_check

@define
class InventoryBase(InventoryInterface):
    capacity: int = field(default=4, validator=capacity_check)
    inventory: List[ItemBase] = field(factory=list)
    validator: InventoryValidator = field(factory=InventoryValidator)
        
    def __attrs_post_init__(self):
   
        if self.count() > self.capacity:
            raise CapcityExceeded(
                f"Number of items ({len(self.inventory)}) "
                f"cannot exceed capacity ({self.capacity})."
            )

    @override
    def add(self, items: List[ItemBase]) -> None:
        
        validated_items = self.validator.validate_items()

        if len(self.inventory) + len(items) > self.capacity:
            raise CapcityExceeded("Player's Inventory has Reached it's Capacity")
        
        self.inventory.extend(validated_items)

    @override
    def remove(self, items: List[ItemBase]) -> None:
        
        validated_items = self.validator.validate_items(items)

        for vm in validated_items:
            if vm in self.inventory:
                self.inventory.remove(vm)
            else:
                raise ItemNotFound(f"Item {vm} not found in Inventory")

    @override
    def show(self) -> List[ItemBase]:
        return self.inventory

    @override
    def has(self, item: ItemBase) -> bool:
        return item in self.inventory
    
    @override
    def count(self) -> int:
        return len(self.inventory)
    
    @override
    def space(self) -> int: #return total free Capacity
        return self.capacity - self.count()

    @override
    def clear(self) -> None:
        self.inventory.clear()