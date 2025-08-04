from ..Effect._effect_handler import _EffectHandler as EffectHandler
from ...GameConstant.bullet import Bullet
from ..Shotgun._magazine import _Magazine as Magazine
from ..Shotgun._shell import _Shell as Shell
from pydantic import BaseModel, Field, PrivateAttr, model_validator
from ...GameException.shotugn_exception import ShotgunException
from typing import Optional

class Shotgun(BaseModel):

    """
    Represents a modular shotgun system with shell-based effects and controlled internal state.

    This class encapsulates core gameplay logic related to lives, blank shells, and shell handling.
    Internal components such as `Magazine`, `Shell`, and `EffectHandler` are auto-constructed
    and are not intended for manual override. This ensures centralized delegation and consistent
    state management.

    Attributes:
        lives (int): Number of lives remaining. Immutable.
        blanks (int): Number of blank shells available. Immutable.
        magazine (Magazine): Internal shell queue. Auto-instantiated.
        shell (Shell): Currently loaded shell. Auto-instantiated.
        effects (Shell): Active shell effects. Auto-instantiated.
        _dmg (int): Private damage value used internally by game logic.

    Model Configuration:
        arbitrary_types_allowed (bool): Enabled to support non-standard component instantiation.

    Notes:
        - Manual injection of `magazine`, `shell`, or `effects` will raise validation errors.
        - Game logic components follow strict ownership delegation.
        - Internal validation ensures safe and predictable instantiation behavior.
    """

    lives: int = Field(default = 4, frozen=True)
    blanks: int = Field(default= 4, frozen=True)
    magazine: Optional[Magazine] = None #Separately Set the values - don't only rely on Constructor
    shell: Shell = Field(default_factory=Shell)
    effects: EffectHandler = Field(default_factory=EffectHandler)
    _dmg: int = PrivateAttr(default=1)
      
    model_config = {
        "arbitrary_types_allowed": True # Fixed EffectHandler Validation Problem!
    }

    @model_validator(mode="before")
    @classmethod
    def _forbiddenInjection(cls, values):
        forbidden_fields = ["magazine", "effects", "shell"]
        for field in forbidden_fields:
            if field in values:
                raise TypeError(f"Field '{field}' must not be manually provided.")
        return values
    
    @model_validator(mode="after")
    def _initiateMagazine(self) -> "Shotgun":

        self.magazine = Magazine(lives=self.lives, blanks=self.blanks)
        return self

    def loadChamber(self) -> Bullet:
        
        bullet = self.magazine.takeOutBullet()
        self.shell.load(bullet)

        return bullet
        
    @property
    def liveDamage(self) -> int:
        return self._dmg 
            
    def setliveDamage(self,new_dmg) -> None:

        if(new_dmg <=0):
            raise ShotgunException(f"Damage Should be Positive | It Can not be {new_dmg}")
        
        self._dmg = new_dmg

    def __str__(self):
        return f"Magazine: {self.magazine.getMagazine}, Damage: {self._dmg}, effects: {self.effects.show}" #need more working!
    