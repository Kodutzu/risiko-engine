from attrs import define, field, setters
from typing import override, Optional

from .validator import charge_checker
from ..inventory.base import InventoryBase
from ..inventory.interface import InventoryInterface

@define
class PlayerBase:

    _id: str = field(on_setattr=setters.frozen, alias="player_id")
    _charges: Optional[int] = field(validator=charge_checker, alias="charges")
    _inventory: Optional[InventoryInterface] = field(factory=InventoryBase, alias="inventory")

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

    
