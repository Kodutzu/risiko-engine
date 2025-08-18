
from ...constants.usable_entity import UsableEntity
from pydantic import Field
from pydantic.dataclasses import dataclass
from .exceptions import EffectException

@dataclass
class Effect:

    entity: UsableEntity
    turns: int = Field(default=1, gt=0)

    @property
    def name(self) -> UsableEntity: 
        return self.entity.name

    @property
    def turn(self) -> None:
        return self.turns

    def reduce_turn(self,red=1) -> None:
        if(self.turns < red):
            raise EffectException(f"Invalid Args, It should be Positive - Got {red}")
        self.turns -= red

    def __repr__(self) -> str:
        return f"Effect(entity={self.entity.name}, turns={self.turns})"
    



