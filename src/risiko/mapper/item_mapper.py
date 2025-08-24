from .interface import MapperInterface
from ..core.item.interface import ItemInterface
from ..core.item.snapshot import ItemSnapshot
from typing import override

class ItemMapper(MapperInterface):
    
    @staticmethod
    @override
    def disassemble(
        interface: ItemInterface,
        snapshot: ItemSnapshot = ItemSnapshot
        ) -> ItemSnapshot:

        return snapshot(
            entity=interface.entity
            )
 
