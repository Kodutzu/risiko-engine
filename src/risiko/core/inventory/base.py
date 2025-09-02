from typing import List, override
from attrs  import define, field


from .interface import InventoryInterface
from ..item.interface import ItemInterface
from .exceptions import CapacityExceeded
from .validator import capacity_check

@define
class InventoryBase(InventoryInterface):
    
    _inventory: List[ItemInterface] = field(factory=list, alias="inventory")
    _capacity: int = field(default=4, validator=capacity_check, alias="capacity")

        
    def __attrs_post_init__(self):
   
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
