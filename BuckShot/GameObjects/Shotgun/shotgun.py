from ..Effect._effect_handler import _EffectHandler as EffectHandler
from ...GameConstant.bullet import Bullet
from ..Shotgun._magazine import _Magazine as Magazine
from ..Shotgun._shell import _Shell as Shell
from pydantic import BaseModel, Field, PrivateAttr, model_validator, PrivateAttr
from ...GameException.ObjectException.shotugn_exception import ShotgunException

class Shotgun(BaseModel):

    lives: int = Field(default = 4, frozen=True)
    blanks: int = Field(default= 4, frozen=True)
    _magazine: Magazine = PrivateAttr()
    _shell: Shell = PrivateAttr(default_factory=Shell)
    _effects: EffectHandler = PrivateAttr(default_factory=EffectHandler)
    _live_dmg: int = PrivateAttr(default=1)
      
    
    @model_validator(mode="after")
    def _initiateMagazine(self) -> "Shotgun":

        self._magazine = Magazine(lives=self.lives, blanks=self.blanks)

        return self
    
    @property
    def magazine(self): return self._magazine

    @property
    def shell(self): return self._shell
    
    @property
    def effects(self): return self._effects

    def loadChamber(self) -> Bullet:
        
        bullet = self._magazine.takeOutBullet()
        self._shell.load(bullet)

        return bullet
        
    @property
    def liveDamage(self) -> int:
        return self._live_dmg 
            
    def setliveDamage(self,new_dmg) -> None:

        if new_dmg < 0: raise ValueError("Damage cannot be negative")
        
        self._live_dmg = new_dmg

    def __repr__(self) -> str:
        return f"<Shotgun {self.lives} Live /{self.blanks} Blanks dmg={self._live_dmg}>"

    