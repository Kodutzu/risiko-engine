from ..core.inventory.base import InventoryBase
from ..core.inventory.interface import InventoryInterface
from ..core.inventory.snapshot import InventorySnapshot
from .interface  import FactoryInterface

class InventoryFactory(FactoryInterface):

    @staticmethod
    def assemble(
        live_snapshot: InventorySnapshot, 
        live_class: InventoryInterface = InventoryBase
    ) -> InventoryInterface:
        
        return live_class(
            inventory= live_snapshot.item_list,
            capacity= live_snapshot.capacity
        )
