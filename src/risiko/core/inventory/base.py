from typing import List, override, final
from attrs  import define, field,setters
from attrs.validators import instance_of


from .interface import InventoryInterface
from ..item.interface import ItemInterface
from .exceptions import CapacityExceeded

@define
class InventoryBase(InventoryInterface):
    
    _inventory: List[ItemInterface] = field(factory=list, validator=instance_of(list), alias="inventory")
    _capacity: int  = field(default=4, on_setattr=setters.frozen, converter=int, alias="capacity")


    def __attrs_post_init__(self):
   
        if self._capacity is not None:

            if len(self._inventory) > self._capacity:
                raise CapacityExceeded(
                    f"Number of items ({len(self._inventory)}) "
                    f"cannot exceed capacity ({self._capacity})."
                )
    @property
    @override
    @final
    def inventory(self) -> List[ItemInterface]:
        return self._inventory
    

    @property
    @override
    @final
    def capacity(self) -> int:
        return self._capacity
