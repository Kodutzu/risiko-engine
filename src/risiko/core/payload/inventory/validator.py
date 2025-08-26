from ..item.interface import ItemInterface
from typing import List, Any
from ..item.exceptions import InvalidItem
from ..inventory.exceptions import InvalidList, CapacityExceeded
from attrs import Attribute


class InventoryValidator:

    @staticmethod
    def validate_items(items: List[ItemInterface]) -> List[ItemInterface]:
        if not isinstance(items, list):
            raise InvalidList("Item should be encapsulated within a List")
        for item in items:
            if not isinstance(item, ItemInterface):
                raise InvalidItem(f"Invalid item type: {type(item)}")
        return items
    
    @staticmethod
    def capacity_check(instance: Any,attribute: Attribute, value: int) -> None:

        if value <4:
            raise CapacityExceeded(f"{attribute.name} must be greater than or equal to 4")