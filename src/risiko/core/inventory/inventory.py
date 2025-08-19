from typing import List, Union
from pydantic import BaseModel, PrivateAttr,Field
from ..item.item import Item 
from .exceptions import CapcityExceeded, ItemNotFound
from ..item.exceptions import InvalidItem

class Inventory(BaseModel):
    _inventory: List[Item] = PrivateAttr(default_factory=list)
    capacity: int = Field(default=4, ge=4)


    def add(self, items: Union[List[Item], Item], force=False) -> None:
        
        validated_items = self._validate_items(items)

        if (not force) and len(self._inventory) + len(items) > self.capacity:
            raise CapcityExceeded("Player's Inventory has Reached it's Capacity")
        
        self._inventory.extend(validated_items)

    def remove(self, items: Union[List[Item], Item]) -> None:
        
        validated_items = self._validate_items(items)

        for vm in validated_items:
            if vm in self._inventory:
                self._inventory.remove(vm)
            else:
                raise ItemNotFound(f"Item {vm} not found in Inventory")

    def show(self) -> List[str]:
        return [item for item in self._inventory]

    def has(self, item: Item) -> bool:
        return item in self._inventory
    
    def space(self) -> int: #return total free Capacity
        return self.capacity - self.count()
    
    def count(self) -> int:
        return len(self._inventory)

    def clear(self) -> None:
        self._inventory.clear()

    @staticmethod
    def _validate_items(item_objs: List[Item] | Item) -> List[Item]:
        if isinstance(item_objs, Item):
            item_objs = [item_objs]
        for item in item_objs:
            if not isinstance(item, Item):
                raise InvalidItem(f"Invalid item type: {type(item)}")
        return item_objs

    def __repr__(self) -> str:
        return f"Inventory(capacity={self.capacity}, items={self._inventory})"
