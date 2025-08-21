#Handling Inventory - Adding and Removing Items, and managing Inventory Space, many more to come
from ..core.game.snapshot import GameSnapshot
from ..core.inventory.inventory import Inventory
from ..core.item.item import Item
from typing import  List
class InventoryHandler:

    @staticmethod
    def add_item(snapshot: GameSnapshot, player_id: int, items_to_add: List[Item]) -> None:
        
        new_snapshot = snapshot.model_copy(deep=True)
        
        player_to_update = None 
        for player in new_snapshot.players:
            if player.id == player_id:
                player_to_update = player
                break
        else:
            raise Exception("Player not found")
        
        inv = Inventory(inventory=player_to_update.inventory.items, capacity=player_to_update.inventory.capacity)

        inv.add(items_to_add)

        player_to_update.inventory.items = inv
            

    def remove():
        pass

    def show():
        pass

    def has() :
        pass
    
    def space():
        pass
    
    def count():
        pass

    def clear() :
        pass
