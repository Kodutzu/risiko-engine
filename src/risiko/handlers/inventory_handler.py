from ..core.game.snapshot import GameSnapshot
from ..core.player.snapshot import PlayerSnapshot
from ..core.inventory.interface import InventoryInterface
from ..core.item.base import ItemBase
from typing import  List, NoReturn, Union
from ..core.game.snapshot import GameSnapshot
from ..core.player.snapshot import PlayerSnapshot
from ..core.inventory.snapshot import InventorySnapshot
from ..core.inventory.base import InventoryBase



class InventoryFactory:

    @staticmethod
    def create_inventory(inventory_snapshot: InventorySnapshot) -> Union[InventoryBase, InventoryInterface]:
        return InventoryBase(
            inventory=inventory_snapshot.item_list, 
            capacity=inventory_snapshot.capacity
            )


class InventoryHandler:

    @staticmethod
    def add_item(snapshot: GameSnapshot, player_id: int, items_to_add: List[ItemBase]) -> GameSnapshot:
        new_snapshot = snapshot.model_copy(deep=True)
        
        player_to_update = InventoryHandler._get_player(new_snapshot, player_id)
        
        inventory_snapshot = player_to_update.inventory
        
        live_inventory_obj = InventoryFactory.create_inventory(inventory_snapshot)
        
        live_inventory_obj.add(items_to_add)
        
        player_to_update.inventory.item_list = live_inventory_obj.show()
        
        return new_snapshot

    @staticmethod
    def remove_item(snapshot: GameSnapshot, player_id: int, items_to_remove: List[ItemBase]) -> GameSnapshot:
        new_snapshot = snapshot.model_copy(deep=True)
        player_to_update = InventoryHandler._get_player(new_snapshot, player_id)
        
        inventory_snapshot = player_to_update.inventory
        live_inventory_obj = InventoryFactory.create_inventory(inventory_snapshot)
        live_inventory_obj.remove(items_to_remove)
        player_to_update.inventory.item_list = live_inventory_obj.show()
        
        return new_snapshot

    @staticmethod
    def _get_player(snapshot: GameSnapshot, player_id: str) -> Union[PlayerSnapshot, NoReturn]:
        player = snapshot.players.get(player_id)
        if not player:
            raise Exception(f"Player with ID '{player_id}' not found.")
        return player
