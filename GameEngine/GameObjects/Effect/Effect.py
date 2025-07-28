from dataclasses import dataclass
from ..Constant.EffectsType import EffectsType

@dataclass
class Effect:
    type: EffectsType
    turns: int = 1

    def tick(self):
        self.turns -= 1

    def __repr__(self):
        return f"<Effect {self.type.name}: {self.turns} turns>"

  


