from ..Loadout._inventory import _Inventory as Inventory
from ..Effect._effect_handler import _EffectHandler as EffectHandler
from pydantic import BaseModel, Field, field_validator, PrivateAttr
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
    charges: _ChargeMeter = Field(default_factory=_ChargeMeter)
    _inventory: Inventory = PrivateAttr(default_factory=Inventory)
    _effects: EffectHandler = PrivateAttr(default_factory=EffectHandler)   

    @field_validator("charges", mode="before")
    @classmethod
    def chargeCoercion(cls, v):  # Allow `charges=int` to be auto-converted
       
        if isinstance(v, int):
            return _ChargeMeter(value=v)
        return v
    
    @property
    def inventory(self): return self._inventory

    @property
    def effects(self): return self._effects

    
    def __str__(self):
        return (
        f"Player(id={self.id}, charges={self.charges.showCharge}, "
        f"inventory={self.inventory.show}, effects={self.effects.show()}"
        )