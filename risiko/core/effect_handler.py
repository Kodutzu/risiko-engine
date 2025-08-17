from .effect import Effect
from pydantic import PrivateAttr, BaseModel
from typing import List, Dict
from ..exception.effect_exception import EffectException

class EffectHandler(BaseModel): 

    _effects: List[Effect] = PrivateAttr(default_factory=list) 

    def add(self, effect_obj:Effect) -> None:

        if not isinstance(effect_obj, Effect):
            raise EffectException(f"It should be effect, got {effect_obj} as Args")

        for effect in self._effects:

            if effect == effect_obj:

                raise EffectException(f"Effect: {effect_obj} is Already Applied")
      
        self._effects.append(effect_obj)
 
    def show(self, only_active: bool =False) -> Dict[Effect, int]:
        return [
                (effect.item_type.name, effect.turns)
                for effect in self._effects
                if not only_active or effect.showTurn > 0
        ]
    
    def has(self, effect_obj: Effect) -> bool:

        for effect in self._effects:
            if effect == effect_obj:
                return True
        return False
    
    def remove(self, effect_obj: Effect) -> None:

        if not isinstance(effect_obj, Effect):
            raise EffectException(f"It should be effect, got {effect_obj} as Args")

        if effect_obj not in self._effects:
            
            raise EffectException(f"Effect: {effect_obj} is not Applied")
      
        self._effects.remove(effect_obj)
    
    def tickAll(self) -> None:
        """
        Reduces the turns of all effects in the EffectHandler by 1.

        This function iterates over each effect in the EffectHandler and calls the 
        reduceTurn method of the effect, which reduces the turn count by 1.

        This function does not return anything.

        """
        for effect in self._effects:
            effect.reduceTurn()

    def removeExpired(self) -> List[Effect]:
        """
        Removes all expired effects from the EffectHandler and returns them as a list.

        An effect is considered expired if its remaining turns is less than or equal to 0.

        Returns:
            List[Effect]: A list of expired effects.
        """
        expired_effects = [effect for effect in self._effects if effect.showTurn <= 0]
        self._effects = [effect for effect in self._effects if effect.showTurn > 0]

        return expired_effects
       
    # Experimenting with Dunder Method "__contains__"
    def __contains__(self, effect_type) -> bool:

        return effect_type in self._effects