from .interface import EffectorInterface
from ..effect.base import EffectBase
from attrs import define, field
from typing import List, Tuple, override
from .exceptions import EffectNotFound,  DuplicateEffect
from .validator import EffectorValidator

@define
class EffectorBase(EffectorInterface): 

    _effector: List[EffectBase] = field(factory=list, alias="effector")

    @property
    @override
    def effector(self) -> List[Tuple[EffectBase, int]]:

        return [
                (effect.entity, effect.turns)
                for effect in self._effector
               ]  

    @override
    def add(self, effect: EffectBase) -> None:

        validated_effect = EffectorValidator.validate_items(effect)

        if validated_effect in self._effector:

            raise DuplicateEffect(f"{effect} is Already Applied")
      
        self._effector.append(validated_effect)

    @override
    def remove(self, effect: EffectBase) -> None:

        validated_effect = EffectorValidator.validate_items(effect)

        if effect not in self._effector:
            
            raise EffectNotFound(f"Effect: {effect} is not Applied")
      
        self._effector.remove(validated_effect)

    
    def has(self, effect_obj: EffectBase) -> bool:

        return effect_obj in self._effector

    @override
    def reduce_all(self) -> None:

        for effect in self._effector:
            effect.reduce_turn()

    @override
    def remove_expired(self) -> None:

        for effect in self._effector:
            if not effect.is_active:
                self._effector.remove(effect) 

    def clear(self) -> None:

        self._effector.clear()
    
