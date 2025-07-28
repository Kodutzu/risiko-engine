from GameEngine.GameObjects.Constant.Bullet import Bullet
from dataclasses import dataclass,field

@dataclass
class Magazine:
    lives: int = 4
    blanks: int = 4
    _tube: dict = field(init=False)
    _increment: dict = field(init=False)

    def __post_init__(self):
    
        self.__base_tube= {
            Bullet.LIVE: self.lives,
            Bullet.BLANK: self.blanks
        }

        self._increment = {
            Bullet.LIVE: self.lives//2 ,
            Bullet.BLANK: self.blanks//3 
        }   

        self._tube = self.__base_tube.copy()  


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
    
    
    