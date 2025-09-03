from attrs import define, field, setters
from attrs.validators import instance_of, ge
from typing import override, Optional

from ..inventory.base import InventoryBase
from ..inventory.interface import InventoryInterface

@define
class PlayerBase:

    _id: str = field(converter=str,on_setattr=setters.frozen, alias="player_id", )
    _charges: Optional[int] = field(converter=int,validator= ge(0), alias="charges")
    _inventory: Optional[InventoryInterface] = field(factory=InventoryBase, validator=instance_of(InventoryInterface), alias="inventory")

    @property
    @override
    def id(self) -> str:
        return self._id
    
    @property
    @override
    def charges(self) -> int : 
        return self._charges  
    
    @property
    @override
    def inventory(self) -> InventoryInterface:
        return self._inventory

    
