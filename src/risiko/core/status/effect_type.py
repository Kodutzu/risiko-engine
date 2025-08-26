from enum import Enum, auto

class EffectType(Enum):
    CUFFED = auto()
    DOUBLE_DAMAGE = auto()
    DEFECTOR = auto() #After Applying, gives the player an armor for the next turn
