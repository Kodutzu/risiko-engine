from .interface import MapperInterface
from ..core.item.base import ItemBase 
from ..core.item.snapshot import ItemSnapshot
from typing import override

class ItemMapper(MapperInterface):
    
    @staticmethod
    @override
    def to_snapshot(live_item: ItemBase ) -> ItemSnapshot:
        return ItemSnapshot(entity=live_item.entity)
    
    @staticmethod
    @override
    def from_snapshot(snapshot: ItemSnapshot) -> ItemBase:
        return ItemBase(entity=snapshot.entity)
