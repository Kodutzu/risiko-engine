from .interface import ItemInterface
from attrs import define
from ...constants.usable_entity import UsableEntity

@define(frozen=True)
class ItemBase(ItemInterface):
    entity: UsableEntity

    def __repr__(self) -> str:
        return f"Item(entity={self.entity.name})"


