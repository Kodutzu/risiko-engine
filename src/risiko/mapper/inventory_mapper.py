from .interface import MapperInterface
from ..core.inventory.interface import InventoryInterface 
from ..core.inventory.snapshot import InventorySnapshot
from .item_mapper import ItemMapper
from typing import override

class InventoryMapper(MapperInterface):
    
    @staticmethod
    @override
    def disassemble(

        interface: InventoryInterface,
        snapshot: InventorySnapshot = InventorySnapshot
        
          ) -> InventorySnapshot:
        
        return snapshot(
            item_list= [ItemMapper.disassemble(item) for item in interface.inventory], 
            capacity= interface.capacity
            )
    
