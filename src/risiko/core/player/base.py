from attrs import define, field, Factory, setters
from attrs.validators import instance_of, ge
from typing import override, final,  ClassVar, Set

from ..inventory.base import InventoryBase
from ..inventory.interface import InventoryInterface
from .interface import PlayerInterface

@define
class PlayerBase(PlayerInterface):

    _id: str = field(converter=str,on_setattr=setters.frozen, alias="player_id", )
    _charges: int = field(converter=int,validator= ge(0), alias="charges")
    _inventory: InventoryInterface = field(validator=instance_of(InventoryInterface),alias="inventory")
    _existing_ids: ClassVar[Set[str]] = set()

    def __attrs_post_init__(self):

        if self._id in self._existing_ids:
            raise ValueError(f"Player with ID {self._id} already exists.")
        self._existing_ids.add(self._id)

    @property
    @override
    @final
    def id(self) -> str:
        return self._id
    
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

    
