from ..Effect.Effect import _Effect as Effect
from ..Effect.Effecthandler import EffectHandler
from ..Constant.EffectsType import EffectsType
from GameEngine.GameObjects.Constant.Bullet import Bullet
from ._ItemBase import _ItemBase as ItemBase
from ..Shotgun.Shotgun import Shotgun
from ..Player.Player import Player

class Electricity(ItemBase):

    expected_type = Player

    def use(self, user:Player,target:Player):
        
        self.validate(target, Player)

        if user is not target:
            raise Exception("It has to be you")

        user.charges.gain(1)
        return {"Status": f"{user.name} gained a charge"}


class Inverse(ItemBase):
# Only Available in Level - 2
    def inverse(self, gun:Shotgun):

        current_shell = gun.shell.currentShell

        gun.shell.unloadShell()  

        self.inverse_shell = Bullet.BLANK if current_shell == Bullet.LIVE else Bullet.LIVE
        
        gun.shell.loadShell(self.inverse_shell)
        
    
    def use(self, user:Player, target:Shotgun):
        self.validate(target, Shotgun)
        self.inverse(target)
        return self.inverse_shell
    

class HandCuff(ItemBase):

    def cuff(self,target:Player):
        effect_obj = Effect(EffectsType.CUFFED, turns=2)
        target.effects.add(effect_obj)
        return f"{target.name} is handcuffed for next turn."
    
    def use(self,user: Player, target: Player):
        self.validate(target,Player)

        if user is target:
            raise Exception("It can't be you!")
        return self.cuff(target)

class Knife(ItemBase):

    def Sharp(self, gun:Shotgun):
        effect_obj = Effect(EffectsType.Knife)
        gun.effects.add(effect_obj)
        gun.setliveDamage(2)

    def use(self, user: Player, target: Shotgun):
        self.validate(target, Shotgun)
        return self.Sharp(target)

class Deflect(ItemBase): #An Level 3 Item!
    
    def putShield(self, user: Player):

        effect_obj = Effect(EffectsType.Deflect)
        user.effects.add(effect_obj)

    def use(self,  user:Player, target:Player):
        self.validate(target,Player)
        if user is not target:
            raise Exception("it has to be you!")
        
        return self.putShield(target)

class Eject(ItemBase):
    
    def pull(self,gun:Shotgun):

        self.ejected_bullet = gun.shell.unloadShell()

        return f"Ejected {self.ejected_bullet} "

    def use(self, user:Player, target: Shotgun):
        self.validate(target,Shotgun)
        return self.pull(target)

class Magnifier(ItemBase):
    
    def look(self, gun: Shotgun):
        return gun.shell.currentShell

    def use(self,user: Player, target: Shotgun):
        self.validate(target,Shotgun)
        return self.look(target)

