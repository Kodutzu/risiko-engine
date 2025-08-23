from ..item.base import Item
from typing import List, Any
from ..item.exceptions import InvalidItem
from ..inventory.exceptions import InvalidList
from attrs import Attribute


class InventoryValidator:

    
    def validate_items(self,items: List[Item]) -> List[Item]:
        if not isinstance(items, list):
            raise InvalidList("Item should be encapsulated within a List")
        for item in items:
            if not isinstance(item, Item):
                raise InvalidItem(f"Invalid item type: {type(item)}")
        return items
    
def capacity_check(instance: Any,attribute: Attribute, value: int) -> None:

    if value <4:
        raise ValueError(f"{attribute.name} must be greater than or equal to 4")