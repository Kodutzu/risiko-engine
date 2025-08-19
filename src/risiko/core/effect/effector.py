from .effect import Effect
from pydantic import PrivateAttr, BaseModel
from typing import List, Tuple
from .exceptions import EffectNotFound, InvalidEffect, DuplicateEffect

class Effector(BaseModel): 

    _effector: List[Effect] = PrivateAttr(default_factory=list) 

    def add(self, effect: Effect) -> None:

        validated_effect = self._validate_items(effect)

        if validated_effect in self._effector:

            raise DuplicateEffect(f"{effect} is Already Applied")
      
        self._effector.append(validated_effect)

    def remove(self, effect: Effect) -> None:

        validated_effect = self._validate_items(effect)

        if effect not in self._effector:
            
            raise EffectNotFound(f"Effect: {effect} is not Applied")
      
        self._effector.remove(validated_effect)
 
    def show(self, only_active: bool = False) -> List[Tuple[Effect, int]]:

        return [
                (effect.name, effect.turn)
                for effect in self._effector
                if not only_active or effect.turns > 0
               ]
    
    def has(self, effect_obj: Effect) -> bool:

        return effect_obj in self._effector

    
    def tick_all(self) -> None:

        for effect in self._effector:
            effect.reduce_turn()

    def remove_expired(self) -> None:

        for effect in self._effector:
            if effect.turns <= 0:
                self._effector.remove(effect) 

    def clear(self) -> None:

        self._effector.clear()
    
    @staticmethod
    def _validate_items(effect: Effect) -> Effect:

        if not isinstance(effect, Effect):
                raise InvalidEffect(f"Invalid Effect: {type(effect)}")
        return effect