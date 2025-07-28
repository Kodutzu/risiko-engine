from ..Effect.Effecthander import EffectHandler
import random
from ..Constant.Bullet import Bullet
from ._Magazine import Magazine
from ._Shell import Shell
from dataclasses import dataclass, field, InitVar

@dataclass
class Shotgun:
    lives: int = 4
    blanks: int = 4
    magazine: Magazine = field(init=False)
    shell: Shell = field(default_factory=Shell)
    effects: EffectHandler = field(init=False)
    _dmg: int = 1

    def __post_init__(self):

        self.magazine = Magazine(lives=self.lives, blanks=self.blanks)
        self.effects = EffectHandler(self)
    
    
    def __randomBullet(self):
        available_bullets = self.magazine.getAvailablebullet()

        if not {Bullet.BLANK, Bullet.LIVE}.issubset(set(available_bullets)):

            raise Exception("There isn't Enough Bullet to Choose Randomly")
        
        random_bullet = random.choice(available_bullets)
        
        return random_bullet

    def loadChamber(self):

        self.shell.loadInShell(self.__randomBullet())
        self.magazine.takeBullet(self.shell.currentShell)

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
        self.shell.alterShell = None
        return dmg # Return Full Data!
    
    def __str__(self):
        return f"Magazine: {self.magazine.getMagazine}, Damage: {self._dmg}"
    
        
    

        


        