from ..Loadout._inventory import _Inventory as Inventory
from ..Effect._effect_handler import _EffectHandler as EffectHandler
from pydantic import BaseModel, Field,  model_validator, field_validator
from pydantic.dataclasses import dataclass

@dataclass
class _ChargeMeter():
    value: int = Field(default=4, ge=3)

    def gain(self, amt): self.value +=amt
    def lose(self,amt): self.value -=amt 

    @property
    def showCharge(self): return self.value
    def __int__(self): return self.value

class Player(BaseModel):

    """
    Represents a player in the game, with charge meter, item inventory, and active effects.

    This class is responsible for:
    - Holding player-specific state such as name, charge meter, items, and effects.
    - Triggering a shotgun.
    - Validating field assignments safely via Pydantic.
    - Using items against other players or the shotgun.
    
    Fields:
    --------
    name : str
        The immutable name of the player.
    
    charges : _ChargeMeter
        Player's charge meter that can increase or decrease based on game logic.
    
    inventory : Inventory
        A player's item inventory, automatically initialized.
    
    effects : EffectHandler
        Manager for all status effects currently applied to the player.
    
    Methods:
    --------
    trigger(shotgun_obj: Shotgun) -> Bullet
        Fires the shotgun and returns the bullet result.

    useItem(item_obj: ItemBase, user: Player, target: Union[Player, Shotgun]) -> Any
        Applies an item's effect from the user onto the target and removes it from inventory.

    """
    name: str = Field(frozen=True)
    charges: _ChargeMeter = Field(default_factory=_ChargeMeter)
    inventory: Inventory = Field(default_factory=Inventory)
    effects: EffectHandler = Field(default_factory=EffectHandler)   
    model_config = {
        "arbitrary_types_allowed": True
    }

    @field_validator("charges", mode="before")
    @classmethod
    def chargeCoercion(cls, v):  # Allow `charges=int` to be auto-converted
       
        if isinstance(v, int):
            return _ChargeMeter(value=v)
        return v
    
    @model_validator(mode="before")
    @classmethod
    def _forbiddenInjection(cls, values):
        forbidden_fields = ["inventory", "effects"]
        for field in forbidden_fields:
            if field in values:
                raise TypeError(f"Field '{field}' must not be manually provided.")
        return values
    
    def __str__(self):
        return f"Player: {self.name}, Charge: {self.charges.showCharge}, Inventory: {self.inventory.show}, Effects: {self.effects.show()}"