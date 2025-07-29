from ..Loadout.Inventory import Inventory
from ..Effect.Effecthander import EffectHandler
from ..Shotgun.Shotgun import Shotgun
from ..Loadout.Item import ItemBase
from ..Constant.Bullet import Bullet
from typing import Optional
from pydantic import BaseModel, Field, PrivateAttr, model_validator, field_validator


class _ChargeMeter(BaseModel):
    value: int = Field(default=4, ge=3)

    def gain(self, amt): self.value +=amt
    def lose(self,amt): self.value -=amt 
    @property
    def showCharge(self): return self.value
    def __int__(self): return self.value

class Player(BaseModel):
    name: str = Field(frozen=True)
    charges: _ChargeMeter = Field(default_factory=_ChargeMeter)
    inventory: Inventory = Field(default_factory=Inventory)
    effects: Optional[EffectHandler] = None     
    model_config = {
        "arbitrary_types_allowed": True
    }

    @field_validator("charges", mode="before")
    @classmethod
    def convert_charges(cls, v):
        if isinstance(v, int):
            return _ChargeMeter(value=v)
        return v
    
    @model_validator(mode="after")
    def initiatePlayer(self):
        self.inventory = Inventory()
        self.effects = EffectHandler(self)

        return self

    @property
    def name(self):
        return self.name
    
    def trigger(self, shotgun_obj): 
        if not isinstance(shotgun_obj, Shotgun):
             raise TypeError(f"Expected a Shotgun instance, got {type(shotgun_obj).__name__}")
        bullet = shotgun_obj.fire()

        if bullet == 1:
            return 1 #return more 
        else: 
            return 0

    def useItem(self, item_obj, entity_obj):

        if not isinstance(item_obj, ItemBase):
            raise TypeError(f"Expected an Item instance, got {type(item_obj).__name__}")
        
        if not isinstance(entity_obj, Shotgun|Player):
            raise TypeError(f"Expected an Shotgun/Player instance, got {type(entity_obj).__name__}")

        if not self.inventory.has(item_obj):
            raise Exception("This Item Doesn't Exist in the inventory!")
        
        usage = item_obj.use(entity_obj)
        self.inventory.remove(item_obj)
        return usage

    def __str__(self):
        return f"Player: {self.name}, Charge: {self.charges.showCharge}, Inventory: {self.inventory.show}, Effects: {self.effects.list()}"

