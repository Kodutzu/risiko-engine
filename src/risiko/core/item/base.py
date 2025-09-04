from attrs import define, field, setters
from attrs.validators import instance_of
from typing import override, final

from .interface import ItemInterface
from .item_type import ItemType

@define
class ItemBase(ItemInterface):

    _kind: ItemType = field(validator=instance_of(ItemType),on_setattr=setters.frozen, alias="kind")

    @property
    @override
    @final
    def kind(self) -> ItemType:
        return self._kind