
from ...constants.usable_entity import UsableEntity
from pydantic import Field
# from pydantic.dataclasses import dataclass
from attrs import define, field
from .interface import EffectInterface

@define
class EffectBase(EffectInterface):

    entity: UsableEntity
    turns: int = field(default=1)

    @property
    def name(self) -> str: 
        return self.entity.name

    @property
    def turn(self) -> int:
        return self.turns

    def reduce_turn(self,red=1) -> None:
        if(self.turns < red):
            raise ValueError(f"Invalid Args, It should be Positive - Got {red}")
        self.turns -= red

    def __repr__(self) -> str:
        return f"Effect(entity={self.entity.name}, turns={self.turns})"
    



