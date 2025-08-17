from ..constant.bullet import Bullet
from pydantic import BaseModel, Field, model_validator, PrivateAttr
from typing import List, Union
from collections import deque, Counter
from ..exception.shotugn_exception import MagazineException
import random 


class Magazine(BaseModel):
    lives: int = Field(ge=1, frozen=True)
    blanks: int = Field(ge=1, frozen=True)
    __base_tube: List[Bullet] = PrivateAttr(default_factory=list)
    _tube: deque[Bullet] = PrivateAttr(default_factory=deque)

    @model_validator(mode="after")
    def _initiateMagzine(self) -> "Magazine":
        
        self.__base_tube = [Bullet.BLANK]*self.blanks + [Bullet.LIVE]*self.lives
        random.shuffle(self.__base_tube)
        self._tube= deque(self.__base_tube)

        return self 
    
    def reload(self) -> None:
   
        random.shuffle(self.__base_tube)
        self._tube = deque(self.__base_tube)

    def getMagazine(self, as_list=True) -> Union[List, Counter[Bullet, int]]:

        if as_list :
            return [bullet.name for bullet in self._tube ]
        else:
            return Counter(self._tube)

    def hasMixedBullets(self) -> bool:

        return Bullet.LIVE in self._tube and Bullet.BLANK in self._tube
        
    def takeOutBullet(self) -> Bullet:
        
        if not self.hasMixedBullets():
            raise MagazineException("Cannot proceed: Magazine does not have a mix of live and blank shells.")
        
        bullet =  self._tube.popleft()

        return bullet