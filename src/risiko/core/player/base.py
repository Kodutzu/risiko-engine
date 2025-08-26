from attrs import define, field, setters
from .validator import charge_checker
from ..payload.inventory.base import InventoryBase
from ..payload.inventory.interface import InventoryInterface

from typing import override

from .interface import PlayerInterface


@define
class PlayerBase(PlayerInterface):

    _id: str = field(on_setattr=setters.frozen, alias="id")
    _charges: int = field(default=4, validator=charge_checker, alias="charges")
    _inventory: InventoryInterface = field(factory=InventoryBase, alias="inventory")

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
    
    @override
    def gain_charge(self, amt: int) -> None: 

        self._charges += amt

    @override
    def lose_charge(self,amt: int)-> None:
        
        self._charges -=amt 
