from typing import List
from pydantic import BaseModel, PrivateAttr,Field, model_validator
from ..item.item import Item 
from .exceptions import CapcityExceeded, ItemNotFound
from ..item.exceptions import InvalidItem

class Inventory(BaseModel):
    inventory: List[Item] = Field(default_factory=list)
    capacity: int = Field(default=4, ge=4)

    @model_validator(mode="after")
    def _check_inventory(self):
        if len(self.inventory) > self.capacity:
            raise CapcityExceeded("Player's Inventory has already reached it's Capacity")
        return self
    
    def add(self, items: List[Item], force=False) -> None:
        
        validated_items = self._validate_items(items)

        if (not force) and len(self.inventory) + len(items) > self.capacity:
            raise CapcityExceeded("Player's Inventory has Reached it's Capacity")
        
        self.inventory.extend(validated_items)

    def remove(self, items: List[Item]) -> None:
        
        validated_items = self._validate_items(items)

        for vm in validated_items:
            if vm in self.inventory:
                self.inventory.remove(vm)
            else:
                raise ItemNotFound(f"Item {vm} not found in Inventory")

    def show(self) -> List[Item]:
        return self.inventory

    def has(self, item: Item) -> bool:
        return item in self.inventory
    
    def space(self) -> int: #return total free Capacity
        return self.capacity - self.count()
    
    def count(self) -> int:
        return len(self.inventory)

    def clear(self) -> None:
        self.inventory.clear()

    @staticmethod
    def _validate_items(item_objs: List[Item]) -> List[Item]:
        if isinstance(item_objs, list):
            item_objs = [item_objs]
        for item in item_objs:
            if not isinstance(item, Item):
                raise InvalidItem(f"Invalid item type: {type(item)}")
        return item_objs
    

    def __repr__(self) -> str:
        return f"Inventory(capacity={self.capacity}, items={self.inventory})"
