from typing import  List, NoReturn, Union, Callable

from ..core.game.snapshot import GameSnapshot
from ..core.player.snapshot import PlayerSnapshot
from ..core.player.exceptions import PlayerNotFoundException
from ..core.item.interface import ItemInterface
from ..core.inventory.interface import InventoryInterface
from ..core.game.snapshot import GameSnapshot
from ..core.player.snapshot import PlayerSnapshot
from ..factory.inventory_factory import InventoryFactory
from ..mapper.inventory_mapper import InventoryMapper
from .handler_base import HandlerBase

class InventoryHandler(HandlerBase):
    @staticmethod
    def add_item(snapshot: GameSnapshot, player_id: int, items_to_add: List[ItemInterface]) -> GameSnapshot:
        return InventoryHandler._operate_on_inventory(snapshot, player_id, lambda inv: inv.add(items_to_add))

    @staticmethod
    def remove_item(snapshot: GameSnapshot, player_id: int, items_to_remove: List[ItemInterface]) -> GameSnapshot:
        return InventoryHandler._operate_on_inventory(snapshot, player_id, lambda inv: inv.remove(items_to_remove))

    @staticmethod
    def clear_inventory(snapshot: GameSnapshot, player_id: int) -> GameSnapshot:
        return InventoryHandler._operate_on_inventory(snapshot, player_id, lambda inv: inv.cle)

    @staticmethod
    def _operate_on_inventory(snapshot: GameSnapshot, player_id: int, operation: Callable[[InventoryInterface], None]) -> GameSnapshot:
        new_snapshot = snapshot.model_copy(deep=True)
        player_to_update = InventoryHandler._get_player(new_snapshot, player_id)
        
        live_inventory_obj = InventoryFactory.assemble(live_snapshot=player_to_update.inventory)
        operation(live_inventory_obj)
        player_to_update.inventory = InventoryMapper.disassemble(live_inventory_obj)
        
        return new_snapshot

    @staticmethod
    def _get_player(snapshot: GameSnapshot, player_id: str) -> Union[PlayerSnapshot, NoReturn]:
        player = snapshot.players.get(player_id)
        if not player:
            raise PlayerNotFoundException(f"Player with ID '{player_id}' not found.")
        return player
