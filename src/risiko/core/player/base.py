from attrs import define, field, Factory
from attrs.validators import instance_of, ge
from typing import override, final,  Optional

from ..inventory.base import InventoryBase
from ..inventory.interface import InventoryInterface
from .interface import PlayerInterface

@define
class PlayerBase(PlayerInterface):

    _charges: int = field(converter=int,validator= ge(0), alias="charges")
    _inventory: InventoryInterface = field(default=Factory(InventoryBase), validator=instance_of(InventoryInterface), alias="inventory")
    
    @property
    @override
    @final
    def charges(self) -> int : 
        return self._charges

    @charges.setter
    @override
    @final
    def charges(self, value: int) -> None:
        self._charges = value  
    
    @property
    @override
    @final
    def inventory(self) -> InventoryInterface:
        return self._inventory

    
