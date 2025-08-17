from .effect_handler import EffectHandler
from ..constants.bullet import Bullet
from .magazine import Magazine
from .shell import Shell
from pydantic import BaseModel, Field, PrivateAttr

class Shotgun(BaseModel):

    magazine: Magazine
    shell: Shell = Field(default_factory=Shell)
    effects: EffectHandler = Field(default_factory=EffectHandler)
    _live_dmg: int = PrivateAttr(default=1)

    class Config:
        arbitrary_types_allowed = True

    def loadChamber(self) -> Bullet:
        
        bullet = self.magazine.takeOutBullet()
        self.shell.load(bullet)

        return bullet
        
    @property
    def liveDamage(self) -> int:
        return self._live_dmg 
            
    def setliveDamage(self,new_dmg) -> None:

        if new_dmg < 0: raise ValueError("Damage cannot be negative")
        
        self._live_dmg = new_dmg

    def __repr__(self) -> str:
        return f"<Shotgun {self.magazine.lives} Live /{self.magazine.blanks} Blanks dmg={self._live_dmg}>"

    