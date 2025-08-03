from ...GameConstant.bullet import Bullet
from pydantic import BaseModel, Field, model_validator, PrivateAttr

from collections import deque, Counter
from ...GameException.shotugn_exception import MagazineException
import random 

class _Magazine(BaseModel):
    lives: int = Field(ge=1, frozen=True)
    blanks: int = Field(ge=1, frozen=True)

    __base_tube: list[Bullet] = PrivateAttr(default_factory=list)
    _tube: deque[Bullet] = PrivateAttr(default_factory=deque)

    @model_validator(mode="after")
    def _initiateMagzine(self):
        
        self.__base_tube = [Bullet.BLANK]*self.blanks + [Bullet.LIVE]*self.lives
        random.shuffle(self.__base_tube)
        self._tube= deque(self.__base_tube)

        return self 
    
    def reload(self):
   
        random.shuffle(self.__base_tube)
        self._tube.clear() #Empties the tubee
        self._tube.extend(self.__base_tube) # Using the base tube to reload!



    def getMagazine(self, ListOrder=True):

        if ListOrder :
            return [bullet.value for bullet in self._tube ]
        else:
            return Counter(self._tube)

    def isBulletMissing(self):
        if len(self.getMagazine(ListOrder=False)) <=1:
                return True
        return False
        
    def loadNextBullet(self):
        
        if self.isBulletMissing():
            raise MagazineException("Lack of Either Live or Blank")
        bullet = self._tube[0]
        self._tube.popleft()


        return bullet