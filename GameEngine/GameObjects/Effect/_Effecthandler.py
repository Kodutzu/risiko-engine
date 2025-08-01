from ..Constant.EffectsType import EffectsType
from ._Effect import _Effect as Effect
from pydantic import PrivateAttr, BaseModel
from pydantic.dataclasses import dataclass
from typing import TYPE_CHECKING, List
from ..Exception.effectException import EffectException

if TYPE_CHECKING:
    from ..Player.Player import Player
    from ..Shotgun.shotgun import Shotgun


class _EffectHandler(BaseModel): 
    _effects: List[Effect] = PrivateAttr(default_factory=list) 

    def add(self, effect_obj:Effect):

        if not isinstance(effect_obj, Effect):
            raise EffectException("It should be an Effect")

        for effect in self._effects:
            if effect == effect_obj:
                raise EffectException(f"Effect: {effect_obj} is Already Applied")
      
        self._effects.append(effect_obj)

        return "Write Something"
    def show(self, only_active=True):
        return {
            effect.effect_type: effect.turns
            for effect in self._effects
            if not only_active or effect.showTurn > 0
        }
    
    # Experimenting with Dunder Method "__contains__"
    def __contains__(self, effect_type):
        return effect_type in self._effects
    
    def tickAll(self):
        for effect in self._effects:
            effect.reduceTurn(1)

    def removeExpired(self):
        expired_effects = [effect for effect in self._effects if effect.showTurn <= 0]
        self._effects = [effect for effect in self._effects if effect.showTurn > 0]
       
