from attrs import define, field, setters
from typing import override

from .interface import ItemInterface
from .item_type import ItemType

@define
class ItemBase(ItemInterface):

    _entity: ItemType = field(on_setattr=setters.frozen, alias="entity")

    @property
    @override
    def entity(self) -> ItemType:
        return self._entity