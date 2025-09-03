from src.risiko.application.characters.inventory.behaviour import InventoryBehaviour
from src.risiko.core.player.base import PlayerBase
from src.risiko.core.inventory.base import InventoryBase
from src.risiko.core.item.base import ItemBase 

def main():
    player = PlayerBase(player_id=1, charges="1", inventory=InventoryBase(capacity=0))
    print(player)

    



main()