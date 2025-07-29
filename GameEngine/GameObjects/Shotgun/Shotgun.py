from ..Effect.Effecthander import EffectHandler
import random
from ..Constant.Bullet import Bullet
from ._Magazine import _Magazine as Magazine
from ._Shell import _Shell as Shell
from pydantic import BaseModel, Field, PrivateAttr, model_validator
from typing import Optional

class Shotgun(BaseModel):
    lives: int = Field(default = 4, frozen=True)
    blanks: int = Field(default= 4, frozen=True)
    magazine: Magazine = Field(default_factory=Magazine)
    shell: Shell = Field(default_factory=Shell)
    effects: Optional[EffectHandler] = None
    _dmg: int = PrivateAttr(default=1)
      
    model_config = {
        "arbitrary_types_allowed": True # Fixed EffectHandler Validation Problem!
    }

    @model_validator(mode="after")
    def initiateShotgun(self)-> "Shotgun":

        self.magazine = Magazine(lives=self.lives, blanks=self.blanks)
        self.effects = EffectHandler(self)

        return self
    
    
    def __randomBullet(self):
        available_bullets = self.magazine.getAvailablebullet()

        if not {Bullet.BLANK, Bullet.LIVE}.issubset(set(available_bullets)):

            raise Exception("There isn't Enough Bullet to Choose `Randomly` ")
        
        random_bullet = random.choice(available_bullets)
        
        return random_bullet

    def loadChamber(self):


        bullet = self.__randomBullet()
        self.magazine.takeBullet(bullet)
        self.shell.loadShell(bullet)
       

        return "loaded" #return useful data in dict()
    
        
    @property
    def liveDamage(self):
        return self._dmg if self.shell.currentShell == Bullet.LIVE else 0
            
    @liveDamage.setter
    def liveDamage(self,new_dmg):

        if(new_dmg <=0):
            raise Exception("Damage Can't be Zero or less")
        
        self._dmg = new_dmg

        return self._dmg


    def fire(self):
        
        if self.shell.currentShell is None:
            raise Exception("Shell is empty")
       
        dmg = self._dmg if self.shell.currentShell == Bullet.LIVE else 0
        self.shell.unloadShell()
        return dmg # Return Full Data!
    
    def __str__(self):
        return f"Magazine: {self.magazine.getMagazine}, Damage: {self._dmg}"
    
        
    

        


        