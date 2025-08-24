from typing import  List, NoReturn, Union

from ..core.game.snapshot import GameSnapshot
from ..core.player.snapshot import PlayerSnapshot
from ..core.player.exceptions import PlayerNotFoundException
from ..core.item.interface import ItemInterface
from ..core.game.snapshot import GameSnapshot
from ..core.player.snapshot import PlayerSnapshot
from ..factory.inventory_factory import InventoryFactory
from ..mapper.inventory_mapper import InventoryMapper
from .handler_base import HandlerBase

class InventoryHandler(HandlerBase):

    @staticmethod
    def add_item(snapshot: GameSnapshot, player_id: int, items_to_add: List[ItemInterface]) -> GameSnapshot:

        new_snapshot = snapshot.model_copy(deep=True)
        
        player_to_update = InventoryHandler._get_player(new_snapshot, player_id) #get the player to update
        
        inventory_snapshot = player_to_update.inventory #get the player's inventory
        
        live_inventory_obj = InventoryFactory.assemble(live_snapshot=inventory_snapshot) #assemble the inventory into live base object (InventoryBase)
    
        live_inventory_obj.add(items_to_add)
        
        player_to_update.inventory = InventoryMapper.disassemble(live_inventory_obj)
        
        return new_snapshot

    @staticmethod
    def remove_item(snapshot: GameSnapshot, player_id: int, items_to_remove: List[ItemInterface]) -> GameSnapshot:

        new_snapshot = snapshot.model_copy(deep=True)

        player_to_update = InventoryHandler._get_player(new_snapshot, player_id)
        
        inventory_snapshot = player_to_update.inventory

        live_inventory_obj = InventoryFactory.assemble(inventory_snapshot)
        live_inventory_obj.remove(items_to_remove)

        player_to_update.inventory = InventoryMapper.disassemble(live_inventory_obj)
        
        return new_snapshot
    
    @staticmethod
    def clear_inventory(snapshot: GameSnapshot, player_id: int) -> GameSnapshot:
        new_snapshot = snapshot.model_copy(deep=True)
        
        player_to_update = InventoryHandler._get_player(new_snapshot, player_id)
        
        live_inventory_obj = InventoryFactory.assemble(player_to_update.inventory)
        live_inventory_obj.clear()
    
        player_to_update.inventory = InventoryMapper.disassemble()
        
        return new_snapshot

    @staticmethod
    def _get_player(snapshot: GameSnapshot, player_id: str) -> Union[PlayerSnapshot, NoReturn]:
        player = snapshot.players.get(player_id)
        if not player:
            raise PlayerNotFoundException(f"Player with ID '{player_id}' not found.")
        return player
