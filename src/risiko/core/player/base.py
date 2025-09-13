from attrs import define, field, setters, evolve
from attrs.validators import ge
from typing import Final

@define(frozen=True)
class PlayerBase:
    
    _id: Final[str] = field(alias="player_id",converter=str, on_setattr=setters.frozen) 
    _charges: int = field(alias="charges",validator=ge(0), converter=int, )

    @property
    def id(self) -> str:
        return self._id

    @property
    def charges(self) -> int:
        return self._charges

    def lose_charges(self,amt: int) -> "PlayerBase":

        if self.charges <= 0:
            raise Exception("Player is already Dead, you can't lose charges")
        
        new_charge_value = self.charges - amt
        return evolve(self, _charges=new_charge_value)


    def gain_charges(self,  amt: int) -> "PlayerBase":
        
        new_charge_value = self.charges + amt
        return evolve(self, _charges=new_charge_value)
        