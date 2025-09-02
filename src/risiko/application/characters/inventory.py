from typing import List
from attrs import define, field

from ...core.inventory.base import InventoryBase
from ...core.inventory.interface import InventoryInterface
from ...core.item.interface import ItemInterface
from ...core.item.item_type import ItemType
from ...core.inventory.exceptions import CapacityExceeded, ItemNotFound, InvalidItem, InvalidList


@define
class InventoryCharacter:
        
    data: InventoryInterface = field(factory=InventoryBase, alias="data")


    def has_item(self, item_type: ItemType ) -> bool:

        return any(item.entity == item_type for item in self.data.inventory)


    def add(self, items: List[ItemInterface]) -> None:

        validated_items = self._validate_items(items)

        if len(self.data.inventory) + len(validated_items) > self.data.capacity:
            raise CapacityExceeded("Cannot add items: inventory capacity reached.")
        
        self.data.inventory.extend(items)

    def remove(self, items: List[ItemInterface]) -> None:
        
        validated_items = self._validate_items(items)

        for vm in validated_items:
            try:
                self.data.inventory.remove(vm)
            except ValueError:
                raise ItemNotFound(f"Item {vm} not found in Inventory")

    def clear(self) -> None:

        self.data.inventory.clear()


    def _validate_items(items: List[ItemInterface]) -> List[ItemInterface]:
        if not isinstance(items, list):
            raise InvalidList("Item should be encapsulated within a List")
        for item in items:
            if not isinstance(item, ItemInterface):
                raise InvalidItem(f"Invalid item type: {type(item)}")
        return items
