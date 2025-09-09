from attrs import define, field, setters
from attrs.validators import instance_of, ge
from typing import override, final

from .interface import ItemInterface
from .item_type import ItemType

@define(slots=True)
class ItemBase(ItemInterface):

    _kind: ItemType = field(validator=instance_of(ItemType),on_setattr=setters.frozen, alias="kind")
    _duration: int = field(converter=int,validator=ge(0),on_setattr=setters.frozen, alias="duration")

    @property
    @override
    @final
    def kind(self) -> ItemType:
        return self._kind
    
    @property
    @override
    @final
    def duration(self) -> int:
        return self._duration
    
    @override
    @final
    def radiate(self, amt:int) -> None:
        self._duration -= amt
