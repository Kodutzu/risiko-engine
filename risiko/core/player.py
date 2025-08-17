from .inventory import Inventory
from .effect_handler import EffectHandler
from pydantic import BaseModel, Field, field_validator
from pydantic.dataclasses import dataclass

@dataclass
class _ChargeMeter():
    value: int = Field(default=4, ge=3)

    def gain(self, amt): self.value += amt
    def lose(self,amt): self.value -=amt 

    @property
    def showCharge(self): return self.value
    def __int__(self): return self.value

class Player(BaseModel):

    id: int = Field(frozen=True)
    charges: _ChargeMeter = Field(default_factory=_ChargeMeter, description="The player's charge/health")
    inventory: Inventory = Field(default_factory=Inventory)
    effects: EffectHandler = Field(default_factory=EffectHandler)   

    class Config:
        arbitrary_types_allowed = True
        
    @field_validator("charges", mode="before")
    @classmethod
    def chargeCoercion(cls, v):  # Allow `charges=int` to be auto-converted
       
        if isinstance(v, int):
            return _ChargeMeter(value=v)
            
        return v

    def __str__(self):
        return (
        f"Player(id={self.id}, charges={self.charges.showCharge}, "
        f"inventory={self.inventory.show()}, effects={self.effects.show()}"
        )