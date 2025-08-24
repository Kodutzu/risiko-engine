from .interface import ItemInterface
from attrs import define, field, setters
from ...constants.usable_entity import UsableEntity

@define
class ItemBase(ItemInterface):
    _entity: UsableEntity = field(on_setattr=setters.frozen, alias="entity")

    @property
    def entity(self):
        return self._entity

    
