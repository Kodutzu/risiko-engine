from typing import List
from pydantic import BaseModel, PrivateAttr,Field
from .item import Item 
from ...GameException.ObjectException.inventory_exception import InventoryException
from ...GameException.ObjectException.item_exception import ItemException

class _Inventory(BaseModel):
    _items: List[Item] = PrivateAttr(default_factory=list)
    capacity: int = Field(default=4, ge=4)


    def add(self, item_objs:List[Item] | Item, force=False) -> None:

        if isinstance(item_objs, Item):
            item_objs = [item_objs]

        if (not force) and len(self._items) + len(item_objs) > self.capacity:
            raise InventoryException("Player's Inventory has Reached it's Capacity")
        
        self._items.extend(item_objs)

    def remove(self, item_objs:List[Item] | Item) -> None:
        if isinstance(item_objs, Item):
            item_objs = [item_objs]

        for item_obj in item_objs:
            if item_obj in self._items:
                self._items.remove(item_obj)
            else:
                 raise ItemException(f"Item {item_obj} not found in inventory.")

    def show(self) -> List[str]:
        return [item.type_of.name for item in self._items]

    def has(self, item_obj: Item) -> bool:
        return item_obj in self._items
    
    def showFreeCapacity(self) -> int: #return free Capacity
        return self.capacity - len(self._items)
    

    def count(self) -> int:
        return len(self._items)

    def clear(self) -> None:
        self._items.clear()

    def __repr__(self) -> str:
        return f"Inventory(capacity={self.capacity}, items={self.show(readable=True)})"
