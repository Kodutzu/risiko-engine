from attrs import define, field, setters
from attrs.validators import instance_of, ge
from typing import Final

@define
class PlayerBase:
    
    id: Final[str] = field(alias="player_id",converter=str, on_setattr=setters.frozen) 
    charges: int = field(validator=ge(0), converter=int)
