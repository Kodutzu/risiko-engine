from attrs import define, field, setters
from attrs.validators import instance_of, ge
from typing import override, Optional

from ..inventory.base import InventoryBase
from ..inventory.interface import InventoryInterface

@define
class PlayerBase:

    _charges: Optional[int] = field(converter=int,validator= ge(0), alias="charges")
    _inventory: Optional[InventoryInterface] = field(factory=InventoryBase, validator=instance_of(InventoryInterface), alias="inventory")
    
    @property
    @override
    def charges(self) -> int : 
        return self._charges  
    
    @property
    @override
    def inventory(self) -> InventoryInterface:
        return self._inventory

    
