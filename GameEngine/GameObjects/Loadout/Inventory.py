from typing import List
from pydantic import BaseModel,  model_validator, PrivateAttr,Field,  validate_call
from ._ItemBase import _ItemBase as ItemBase
from pydantic.config import ConfigDict 

class Inventory(BaseModel):
    _items: List[ItemBase] = PrivateAttr(default_factory=list)
    capacity: int = Field(default=4, ge=4)
    model_config = ConfigDict(arbitrary_types_allowed=True)

    
    def add(self, item_objs:List[ItemBase] | ItemBase):

        if isinstance(item_objs, ItemBase):
            item_objs = [item_objs]

        if len(self._items) + len(item_objs) > self.capacity:
            raise Exception("Reached Capacity")
        
        self._items.extend(item_objs)

    def remove(self, item_objs:List[ItemBase] | ItemBase):
        if isinstance(item_objs, ItemBase):
            item_objs = [item_objs]

        for item_obj in item_objs:
            if item_obj in self._items:
                self._items.remove(item_obj)
            else:
                 raise Exception(f"Item {item_obj} not found in inventory.")

    def has(self, item_obj: ItemBase) -> bool:
        return item_obj in self._items
    
    @property
    def freeCapacity(self): #return free Capacity
        return self.capacity - len(self._items)
    
    @property
    def show(self) -> List[str]:
        return [str(item) for item in self._items]

    @property
    def count(self) -> int:
        return len(self._items)

    def clear(self):
        self._items.clear()

    def __str__(self):
        return f"Inventory({', '.join(self.show)})"
