from ..Effect.Effect import _Effect as Effect
from ..Constant.EffectsType import EffectsType
from GameEngine.GameObjects.Constant.Bullet import Bullet
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
#@dataclass - Use it!
#working on the Object Error Handling
#Working on Pyandtic Model
class ItemBase(ABC):

    def __init__(self):
        self.name = self.__class__.__name__

    @abstractmethod
    def use(self,obj):
        pass
    def __eq__(self, other):
        return isinstance(other, self.__class__) 
    
    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.__class__) 

class Electricity(ItemBase):

    def use(self, shooter_obj,charge=1):
      

        shooter_obj.charges.gain(1)
        return {"Status": f"{shooter_obj.name} gained a charge"}


class Inverse(ItemBase):
# Only Available in Level - 2
    def inverse(self, shotgun_obj):

        self.current_shell = shotgun_obj.shell
    
        self.inverse_shell = Bullet.BLANK if self.current_shell == Bullet.LIVE else Bullet.LIVE

        shotgun_obj.shell = self.inverse_shell

       
    
    def use(self, shotgun_obj):
        self.inverse(shotgun_obj)

        return self.inverse_shell
class HandCuff(ItemBase):

    def cuff(self,target_obj):
        effect_obj = Effect(EffectsType.CUFFED, turns=2)
        target_obj.effects.add(effect_obj)
        return f"{target_obj.name} is handcuffed for next turn."
    
    def use(self,target_obj):
        return self.cuff(target_obj)

class Knife(ItemBase):

    def Sharp(self, shotgun_obj,dmg=2):
        effect_obj = Effect(EffectsType.Knife)
        shotgun_obj.effects.add(effect_obj)
        shotgun_obj.damage = dmg

    def use(self, shotgun_obj):

        return self.Sharp(shotgun_obj)

class Deflect(ItemBase):
    
    def putShield(self, shooter_obj):

        effect_obj = Effect(EffectsType.Deflect)
        shooter_obj.effects.add(effect_obj)

    def use(self,  shooter_obj):

        return self.putShield(shooter_obj=shooter_obj)

class Eject(ItemBase):
    
    def pull(self,shotgun_obj):

        shotgun_obj.shell = None
        return 1

    def use(self, shotgun_obj):
        return self.pull(shotgun_obj=shotgun_obj)

class Magnifier(ItemBase):
    
    def look(self, shotgun_obj):
        return shotgun_obj.shell

    def use(self,shotgun_obj):
        return self.look(shotgun_obj=shotgun_obj)

