#Inventory character Depends on it
#Using Strategy Pattern to implement Item's Effect Logic
#Implement Functional Strategy Pattern, where using Functions, instead of of classes and object 
#Use attrs for Memory Efficiency
from attrs import define, field
from attrs.validators import instance_of
from typing import TYPE_CHECKING, Union

from ...core.item.interface import ItemInterface
from ..characters.player.behaviour import PlayerBehaviour
from ..characters.shotgun.behaviour import ShotgunBehaviour 

if TYPE_CHECKING:
    from .strategy.interface import ItemInstructInterface

@define
class ItemEffect: #changing the Name
    ...

    _item_kind: ItemInterface = field(validator=instance_of(ItemInterface), alias="item_kind")
    _strategy: ItemInstructInterface = field(repr=False)


    

    