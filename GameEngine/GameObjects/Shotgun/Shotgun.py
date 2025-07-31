from ..Effect._Effecthandler import _EffectHandler as EffectHandler
import random 
from ..Constant.Bullet import Bullet
from ..Shotgun._magazine import _Magazine as Magazine
from ..Shotgun._shell import _Shell as Shell
from pydantic import BaseModel, Field, PrivateAttr, model_validator
from GameEngine.GameObjects.Exception.shotgunException import ShotgunException
from ..ResponseModels.shotgun_response import ShotgunFireResponse,ShotgunLoad,ShotgunReloadResponse,ShotgunShellResponse, shotgunDamageResponse

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
    magazine: Magazine = Field(default_factory=Magazine)
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
    def _initiateShotgun(self)-> "Shotgun":

        self.magazine = Magazine(lives=self.lives, blanks=self.blanks)
        self.effects = EffectHandler() # Add "self" passable
        
        return self
    

    def loadChamber(self):

        try:
            bullet = self.magazine.loadNextBullet()
            self.shell.loadShell(bullet)

            return ShotgunLoad(
                success=True,
                load_in_chamber=True,
                load_in_shell=True,
                msg="Shell Has been Loaded into Chamber",
                bullet_type=bullet,
                damage=self.liveDamage
            )
        
        except Exception as e: 
            return e
       
        
    @property
    def liveDamage(self):
        return self._dmg 
            
    def setliveDamage(self,new_dmg):

        if(new_dmg <=0):
            raise ShotgunException("Damage Can't be Zero or less")
        
        old_dmg = self._dmg
        self._dmg = new_dmg

        return shotgunDamageResponse(
            old_damage=old_dmg,
            new_damage=self._dmg
        )


    def _fire(self):
        
        if self.shell.currentShell is None:
            raise ShotgunException("Shell is empty")
       
        bullet = self.shell.currentShell
        self.shell.unloadShell()
        return ShotgunFireResponse(
            success=True,
            fired=True,
            msg ="Bullet is Fired",
            bullet_type=bullet,
            damage=self.liveDamage,
            effects_triggered=self.effects.show(),
        )
    
    def __str__(self):
        return f"Magazine: {self.magazine.getMagazine}, Damage: {self._dmg}"
    
        
    

        


        