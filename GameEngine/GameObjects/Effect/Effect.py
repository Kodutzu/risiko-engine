from pydantic import BaseModel
from ..Constant.EffectsType import EffectsType
from pydantic import Field

class _Effect(BaseModel):

    effect_type: EffectsType = Field(frozen=True)
    turns: int = Field(default=1, gt=0, frozen=True)

    @property
    def showType(self): 
        return self.effect_type

    @property
    def showTurn(self) -> None:
        return self._turns
    

    def reduceTurn(self,red) -> None:
        if(self._turns < red):
            raise Exception(f"You can't make turns/duration in Negative")
        self._turns -= red

    def __repr__(self):
        return f"<Effect {self.effect_type.name}: {self._turns} turns>"

  


