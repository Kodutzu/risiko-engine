from typing import List, override, Optional
from attrs  import define, field,setters


from .interface import InventoryInterface
from ..item.interface import ItemInterface
from .exceptions import CapacityExceeded

@define
class InventoryBase(InventoryInterface):
    
    _inventory: Optional[List[ItemInterface]] = field(factory=list, alias="inventory")
    _capacity: Optional[int]  = field(default=4, on_setattr=setters.frozen, alias="capacity")


    def __attrs_post_init__(self):
   
        if self._capacity is not None:

            if len(self._inventory) > self._capacity:
                raise CapacityExceeded(
                    f"Number of items ({len(self._inventory)}) "
                    f"cannot exceed capacity ({self._capacity})."
                )
    @property
    @override
    def inventory(self) -> List[ItemInterface]:
        return self._inventory
    

    @property
    @override
    def capacity(self) -> int:
        return self._capacity
