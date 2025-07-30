from GameEngine.GameObjects.Constant.Bullet import Bullet
from typing import Dict
from pydantic import BaseModel, Field, model_validator, PrivateAttr
from collections import deque, Counter
import random 
class _Magazine(BaseModel):
    lives: int = Field(default=4, ge=1, frozen=True)
    blanks: int = Field(default=4, ge=1, frozen=True)

    __base_tube: list[Bullet] = PrivateAttr(default_factory=dict)
    _tube: deque[Bullet] = PrivateAttr(default_factory=dict)



    @model_validator(mode="after")
    def initiateMagzine(self):
        
        self.__base_tube = [Bullet.BLANK]*self.blanks + [Bullet.LIVE]*self.lives
        random.shuffle(self.__base_tube)
        self._tube= deque(self.__base_tube)

        return self 
    
    def reload(self):
   
        random.shuffle(self.__base_tube)
        self._tube.clear() #Empties the tubee
        self._tube.extend(self.__base_tube) # Using the base tube to reload!
        
    @property
    def getMagazine(self):
        return Counter(self._tube)

    def isBulletMissing(self):
        for count in self.getMagazine.values():
            if count <=0:
                return True
        return False
        
    def loadNextBullet(self):
        
        if self.isBulletMissing():
            raise Exception("Lack of Live and Blank Bullet")
        bullet = self._tube[0]
        self._tube.popleft()


        return bullet  #return info - took out live bullet! 
    