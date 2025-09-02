from .interface import ItemInterface
from attrs import define, field, setters
from .item_type import ItemType

@define
class ItemBase(ItemInterface):
    _entity: ItemType = field(on_setattr=setters.frozen, alias="entity")

    @property
    def entity(self) -> ItemType:
        return self._entity