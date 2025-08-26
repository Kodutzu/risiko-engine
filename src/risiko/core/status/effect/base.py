from attrs import define, field, setters
from typing import override


from .interface import EffectInterface
from .validator import is_not_negative
from ..effect_type import EffectType

@define
class EffectBase(EffectInterface):

    _entity: EffectType = field(on_setattr=setters.frozen, alias="entity")
    _turns: int = field(default=1, validator=is_not_negative, alias="turns")


    @property
    @override
    def entity(self) -> EffectType:
        return self._entity
    
    @property
    @override
    def turns(self) -> int:
        return self._turns
    
    @property
    @override
    def is_active(self) -> bool:
        return self._turns > 0
    
    @override
    def reduce_turn(self,red=1) -> None:
        if red <= 0:
            raise ValueError(f"can not redcue by {red}")
        self._turns -= red
