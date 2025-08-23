from .interface import PlayerInterface
from attrs import define, field,  setters
from .validator import is_positive

@define(frozen=True)
class PlayerBase(PlayerInterface):

    id: str = field(on_setattr=setters.frozen)
    charges: int = field(default=4, validator=is_positive)

    @property
    def charge(self) -> int : 
        return self.charges  
    
    def gain_charge(self, amt: int) -> None: 
        self.charges += amt
    def lose_charge(self,amt: int)-> None: 
        self.charges -=amt 


    def __repr__(self) -> str:
        return f"PlayerBase(id={self.id}, charges={self.charges})"