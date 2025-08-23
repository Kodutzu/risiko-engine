from .interface import EffectorInterface
from ..effect.base import EffectBase
from attrs import define, field
from typing import List, Tuple
from .exceptions import EffectNotFound, InvalidEffect, DuplicateEffect

@define
class Effector(EffectorInterface): 

    effector: List[EffectBase] = field(factory=list) 

    def add(self, effect: EffectBase) -> None:

        validated_effect = self._validate_items(effect)

        if validated_effect in self.effector:

            raise DuplicateEffect(f"{effect} is Already Applied")
      
        self.effector.append(validated_effect)

    def remove(self, effect: EffectBase) -> None:

        validated_effect = self._validate_items(effect)

        if effect not in self.effector:
            
            raise EffectNotFound(f"Effect: {effect} is not Applied")
      
        self.effector.remove(validated_effect)
 
    def show(self, only_active: bool = False) -> List[Tuple[EffectBase, int]]:

        return [
                (effect.name, effect.turn)
                for effect in self.effector
                if not only_active or effect.turns > 0
               ] # This line was not part of the selection, but it uses _effector. Should it be changed to self.effector?
    
    def has(self, effect_obj: EffectBase) -> bool:

        return effect_obj in self.effector

    
    def tick_all(self) -> None:

        for effect in self.effector:
            effect.reduce_turn()

    def remove_expired(self) -> None:

        for effect in self.effector:
            if effect.turns <= 0:
                self.effector.remove(effect) 

    def clear(self) -> None:

        self.effector.clear()
    
    @staticmethod #Moving it to effector/validator.py
    def _validate_items(effect: EffectBase) -> EffectBase:

        if not isinstance(effect, EffectBase):
                raise InvalidEffect(f"Invalid Effect: {type(effect)}")
        return effect