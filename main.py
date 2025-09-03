from src.risiko.application.characters.inventory.behaviour import InventoryBehaviour
from src.risiko.core.inventory.base import InventoryBase
from src.risiko.core.item.item_type import ItemType
from src.risiko.core.item.base import ItemBase 


def main():
    inventory = InventoryBehaviour(data=InventoryBase(capacity=4))
    inventory.remove([ItemBase(entity=ItemType.CHARGER)])
    inventory.add([ItemBase(entity=ItemType.CHARGER)])

    print(inventory.show())
    print(inventory)


main()