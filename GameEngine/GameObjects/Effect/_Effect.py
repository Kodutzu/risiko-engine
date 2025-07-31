
from ..Constant.EffectsType import EffectsType
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..Exception.effectException import EffectException

@dataclass(frozen=True)
class _Effect:

    effect_type: EffectsType 
    turns: int = Field(default=1, gt=0)

    @property
    def showType(self): 
        return self.effect_type

    @property
    def showTurn(self) -> None:
        return self.turns
    

    def reduceTurn(self,red) -> None:
        if(self.turns < red):
            raise EffectException(f"You can't make turns/duration in Negative")
        self._turns -= red

    def __repr__(self):
        return f"<Effect {self.effect_type.name}: {self.turns} turns>"
    



