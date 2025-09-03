from typing import List
from ....core.inventory.exceptions import InvalidItem, InvalidList
from ....core.item.interface import ItemInterface   

class InventoryValidator:

    @staticmethod
    def validate_items(items: List[ItemInterface]) -> List[ItemInterface]:
        if not isinstance(items, list):
            raise InvalidList("Item should be encapsulated within a List")
        for item in items:
            if not isinstance(item, ItemInterface):
                raise InvalidItem(f"Invalid item type: {type(item)}")
        return items
