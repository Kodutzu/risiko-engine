from ...GameConstant.item_type import ItemType
from ..Effect._effect import _Effect as Effect
from pydantic import PrivateAttr, BaseModel
from pydantic.dataclasses import dataclass
from typing import List
from ...GameException.effect_exception import EffectException

class _EffectHandler(BaseModel): 
    _effects: List[Effect] = PrivateAttr(default_factory=list) 

    def add(self, effect_obj:Effect):

        if not isinstance(effect_obj, Effect):
            raise EffectException(f"It should be effect, got {effect_obj} as Args")

        for effect in self._effects:

            if effect == effect_obj:

                raise EffectException(f"Effect: {effect_obj} is Already Applied")
      
        self._effects.append(effect_obj)

     
    def show(self, only_active=False):
        return {
            effect.item_type: effect.turns
            for effect in self._effects
            if not only_active or effect.showTurn > 0
        }
    
    # Experimenting with Dunder Method "__contains__"
    def __contains__(self, effect_type):
        return effect_type in self._effects
    
    def has(self, effect_obj: Effect) -> bool:
        for effect in self._effects:
            if effect == effect_obj:
                return True
        return False
    
    def remove(self, effect_obj: Effect):

        if not isinstance(effect_obj, Effect):
            raise EffectException(f"It should be effect, got {effect_obj} as Args")

        for effect in self._effects:

            if effect != effect_obj:

                raise EffectException(f"Effect: {effect_obj} is not Applied")
      
        self._effects.remove(effect_obj)

    
    def tickAll(self):
        for effect in self._effects:
            effect.reduceTurn(1)

    def removeExpired(self):
        expired_effects = [effect for effect in self._effects if effect.showTurn <= 0]
        self._effects = [effect for effect in self._effects if effect.showTurn > 0]

        return expired_effects
       
