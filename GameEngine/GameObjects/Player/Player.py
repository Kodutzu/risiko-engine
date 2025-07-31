from ..Loadout._Inventory import _Inventory as Inventory
from ..Effect._Effecthandler import _EffectHandler as EffectHandler
from ..Shotgun.shotgun import Shotgun
from ..Loadout._ItemBase import _ItemBase as ItemBase
from ..Constant.Bullet import Bullet
from typing import Union
from pydantic import BaseModel, Field,  model_validator, field_validator
from pydantic.dataclasses import dataclass
from ..ResponseModels.shotgun_response import ShotgunFireResponse, ShotgunErrorResponse

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

    
    @model_validator(mode="after")
    def _initiatePlayer(self):
        self.inventory = Inventory()
        self.effects = EffectHandler()
        # self.effects = EffectHandler(player_effected=self)

        return self

    @property
    def name(self):
        return self.name
    
    def trigger(self, shotgun_obj:Shotgun): 
        if not isinstance(shotgun_obj, Shotgun):
             raise TypeError(f"Expected a Shotgun instance, got {type(shotgun_obj).__name__}")
        
        try:
            bullet, dmg = shotgun_obj._fire()

            return ShotgunFireResponse(
                success=True,
                fired=True,
                msg="Bullet is Fired",
                bullet_type=bullet,
                damage=dmg,
    
                )
        except Exception as e:
            return ShotgunErrorResponse(
                error=str(e)
            )

    def useItem(self, item_obj: ItemBase, user: "Player" , target: Union["Player", Shotgun]):

        if not isinstance(item_obj, ItemBase):
            raise TypeError(f"Expected an Item instance, got {type(item_obj).__name__}")
        
        if not isinstance(user,Player):
            raise TypeError(f"Expected an Player instance, got {type(user).__name__}")
        
        if not isinstance(target,(Shotgun,Player) ):
            raise TypeError(f"Expected an Shotgun/Player instance, got {type(target).__name__}")

        if not self.inventory.has(item_obj):
            raise Exception("This Item Doesn't Exist in the inventory!")
        
        usage = item_obj.use(user,target)
        self.inventory.remove(item_obj)
        return usage

    def __str__(self):
        return f"Player: {self.name}, Charge: {self.charges.showCharge}, Inventory: {self.inventory.show}, Effects: {self.effects.show()}"

