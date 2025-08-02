from ..Effect._effect import _Effect as Effect
from ..Effect._effect_handler import _EffectHandler as Effecthandler
from ...GameConstant.item_type import ItemType
from ...GameConstant.bullet import Bullet
from ._item_base import _ItemBase as ItemBase
from..Exception.player_exception import PlayerException
from ..ResponseClasses.item_response import ItemAppliedResponse

#for typing hintes
from ..Shotgun.shotgun import Shotgun
from ..Player.player import Player

class Electricity(ItemBase):

    expected_type = Player

    def use(self, user:Player,target:Player):
        
        self.validate(target, Player)

        if user is not target:
            raise PlayerException(f"You Can't Apply This Item on {target.__class__.__name__}")
        charge = 1
        user.charges.gain(charge)
        
        return ItemAppliedResponse(
            item_name= ItemType.ELECTRICITY,
            charges_gain=charge,
            user=user,
            target=target

        )


class Inverse(ItemBase):
# Only Available in Level - 2
    def inverse(self, gun:Shotgun):

        current_shell = gun.shell.currentShell

        self.inverse_shell = Bullet.BLANK if current_shell == Bullet.LIVE else Bullet.LIVE

        gun.shell.unloadShell()  

        gun.shell.loadShell(self.inverse_shell)
        
    
    def use(self, user:Player, target:Shotgun):
        self.validate(target, Shotgun)
        self.inverse(target)
        return ItemAppliedResponse(
            item_name=ItemType.INVERSE,
            current_bullet_type=self.inverse_shell,
            user=user,
            target=target
        )
    

class HandCuff(ItemBase):

    def cuff(self,target:Player):
        self.turns = 2
        self.effect_obj = Effect(ItemType.CUFFED, self.turns) # Cuffed, turns =2
        target.effects.add(self.effect_obj)
    
    def use(self,user: Player, target: Player):
        self.validate(target,Player)

        if user is  target:
            raise PlayerException(f"You Can't Apply This Item on {user.__class__.__name__} - who is using it")
        
        self.cuff(target)

        return ItemAppliedResponse(
            item_name=ItemType.CUFFED,
            user=user,      
            target=target,
            effects_applied={self.effect_obj: self.turns},
        )

class Knife(ItemBase):

    def Sharp(self, gun:Shotgun):
        new_dmg = 2
        self.turns = 1
        self.effect_obj = Effect(ItemType.KNIFE, turns=self.turns)
        gun.effects.add(self.effect_obj)
        gun.setliveDamage(new_dmg)

    def use(self, user: Player, target: Shotgun):
        self.validate(target, Shotgun)
        self.Sharp(target)
        return ItemAppliedResponse(
            item_name=ItemType.KNIFE,
            user=user,
            target=target,
            current_bullet_type= target.shell.currentShell,
            damage=target.liveDamage,
            effects_applied={self.effect_obj.item_type:self.turns }
        )

class Eject(ItemBase):
    
    def pull(self,gun:Shotgun):

        self.bullet_present = gun.shell.currentShell #bullet which is there before ejecting!
        self.ejected_bullet = gun.shell.unloadShell() 

    def use(self, user:Player, target: Shotgun):

        self.validate(target,Shotgun)
        self.pull(gun=target)

        return ItemAppliedResponse(
            item_name=ItemType.EJECT,
            user=user,
            target=target,
            shell_ejected=self.bullet_present,
            current_bullet_type= target.shell.currentShell,
        )


class Magnifier(ItemBase):
    
    def look(self, gun: Shotgun):
        return gun.shell.currentShell

    def use(self,user: Player, target: Shotgun):
        self.validate(target,Shotgun)
        bullet = self.look(target)

        return ItemAppliedResponse(
            item_name=ItemType.MAGNIFIER,
            user=user,
            target=target,
            current_bullet_type= bullet,

        )

class Vision(ItemBase):

    def vision(self, gun:Shotgun):
        self.future_bullet = gun.magazine.getMagazine(ListOrder=True)[1]
        return self.future_bullet
    
    def use(self,user:Player, target:Shotgun ):
        self.validate(target, Shotgun)
        self.vision(target)

        return ItemAppliedResponse(
            item_name=ItemType.VISION,
            user=user,
            target=target,
            future_bullet=self.future_bullet
        )

#class Opponnent's shotgun's bullet vision

#class Bomb

#class Deflect(ItemBase): An Level 3 Item!
    
#     def putShield(self, user: Player):

#         effect_obj = Effect(EffectsType.Deflect)
#         user.effects.add(effect_obj)

#     def use(self,  user:Player, target:Player):
#         self.validate(target,Player)
#         if user is not target:
#             raise Exception("it has to be you!")
        
#         return self.putShield(target)