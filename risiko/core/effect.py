
from ..constant.usable_entity import UsableEntity
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..exception.effect_exception import EffectException

@dataclass
class Effect:

    item_type: UsableEntity
    turns: int = Field(default=1, gt=0)

    @property
    def showType(self) -> UsableEntity: 
        return self.item_type

    @property
    def showTurn(self) -> None:
        return self.turns
    

    def reduceTurn(self,red=1) -> int:
        if(self.turns < red):
            raise EffectException(f"Invalid Args, It should be Positive - Got {red}")
        self.turns -= red

        return self.turns

    def __repr__(self) -> str:
        return f"<Effect {self.item_type.name}: {self.turns} turns>"
    



