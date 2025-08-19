from ..inventory.inventory import Inventory
from ..effect.effector import Effector
from pydantic import BaseModel, Field, field_validator
from pydantic.dataclasses import dataclass

@dataclass
class _ChargeMeter:
    value: int = Field(default=4, ge=3)

    def gain(self, amt: int) -> None: self.value += amt
    def lose(self,amt: int)-> None: self.value -=amt 

    @property
    def showCharge(self) -> int : return self.value

class Player(BaseModel):

    id: int = Field(frozen=True)
    charges: _ChargeMeter = Field(default_factory=_ChargeMeter, description="The player's charge/health")
    inventory: Inventory = Field(default_factory=Inventory)
    effector: Effector = Field(default_factory=Effector)   

    class Config:
        arbitrary_types_allowed = True
        
    @field_validator("charges", mode="before")
    @classmethod
    def _charge_coercion(cls, v) -> int:  # Allow `charges=int` to be auto-converted
       
        if isinstance(v, int):
            return _ChargeMeter(value=v)
            
        return v

    def __repr__(self) -> str:
        return f"Player(id={self.id}, charges={self.charges.showCharge})"