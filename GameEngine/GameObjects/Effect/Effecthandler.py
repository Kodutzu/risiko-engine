from ..Constant.EffectsType import EffectsType
from .Effect import _Effect as Effect
from pydantic import PrivateAttr, BaseModel
from pydantic.dataclasses import dataclass
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from ..Player.Player import Player
    from ..Shotgun.Shotgun import Shotgun

# Improving it Overall!
# Object Error Handling!
# Pydantic Model Implementation!



class EffectHandler(BaseModel): # Require Error Handling - where Effect from Effecttype can be added!

    # player_effected: "Player" 
    _effects: List[Effect] = PrivateAttr(default_factory=list) 

    def add(self, effect_obj:Effect):

        if not isinstance(effect_obj, Effect):
            raise Exception("It should be an Effect")

        for effect in self._effects:
            if effect == effect_obj:
                raise Exception(f"Effect: {effect_obj} is Already Applied")
      
        self._effects.append(effect_obj)

    def show(self, only_active=True):
        return [
            {effect.showType: effect.showTurn}
            for effect in self._effects
            if not only_active or effect.showTurn > 0
        ]
    
    # def __contains__(self, effect_type):
    #     return effect_type in self.effects
    
    def tickAll(self):
        for effect in self._effects:
            effect.reduceTurn(1)

    def removeExpired(self):
        expired_effects = [effect for effect in self._effects if effect.showTurn <= 0]
        self._effects = [effect for effect in self._effects if effect.showTurn > 0]
       
