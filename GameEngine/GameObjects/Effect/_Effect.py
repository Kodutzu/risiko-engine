
from ...GameConstant.item_type import ItemType
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..Exception.effect_exception import EffectException

@dataclass()
class _Effect:

    item_type: ItemType
    turns: int = Field(default=1, gt=0, frozen=True)

    @property
    def showType(self): 
        return self.item_type

    @property
    def showTurn(self) -> None:
        return self.turns
    

    def reduceTurn(self,red) -> None:
        if(self.turns < red):
            raise EffectException(f"You can't make turns/duration in Negative")
        self.turns -= red

    def __repr__(self):
        return f"<Effect {self.item_type.name}: {self.turns} turns>"
    



