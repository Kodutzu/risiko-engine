from GameEngine.GameObjects.Constant.Bullet import Bullet
from typing import Dict
from pydantic import BaseModel, Field, model_validator, PrivateAttr
class _Magazine(BaseModel):
    lives: int = Field(default=4, ge=1)
    blanks: int = Field(default=4, ge=1)
    __base_tube: Dict[Bullet, int] = PrivateAttr(default_factory=dict)
    _tube: Dict[Bullet, int] = PrivateAttr(default_factory=dict)
    _increment: Dict[Bullet, int] = PrivateAttr(default_factory=dict)


    @model_validator(mode="after")
    def initiateMagzine(self):
    
        self.__base_tube= {
            Bullet.LIVE: self.lives,
            Bullet.BLANK: self.blanks
        }

        self._increment = {
            Bullet.LIVE: self.lives//2 ,
            Bullet.BLANK: self.blanks//3 
        }   

        self._tube = self.__base_tube.copy() 

        return self 


    def reload(self):
        
        for bullet in self.__base_tube.keys():
            self.__base_tube[bullet] += self._increment[bullet]

        self._tube = self.__base_tube.copy()
        
    @property
    def getMagazine(self):
        return self._tube

    def getAvailablebullet(self):
        return [bullet for bullet, count in self._tube.items() if count >0]
        
    def takeBullet(self, bullet_type):

        if self._tube.get(bullet_type,0) <=0:
            raise Exception(f"Failed to {bullet_type} within the Magazine ")
        
        self._tube[bullet_type] -=1

        return bullet_type
    
    
    