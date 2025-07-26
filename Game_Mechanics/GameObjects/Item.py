from Game_Mechanics.GameObjects.Effect import Effect, EffectsType
class Electricity():


    def use(self, shooter_obj,charge=1):
        shooter_obj.charge = charge

        return {"Status": f"{shooter_obj.name} gained a charge"}


class Inverse():
# Only Available in Level - 2
    def inverse(self, shotgun_obj):

        self.current_shell = shotgun_obj.shell() 
        if(self.current_shell == "STUN"):
            raise Exception("Can't Inverse STUN")
        
        else:
            self.inverse_shell = "Blank" if self.current_shell == "LIVE" else  "LIVE"

        shotgun_obj.shell(self.inverse_shell) 

       
    
    def use(self, shotgun_obj):
        self.inverse(shotgun_obj)

        return 1
class HandCuff():

    def cuff(self,target_obj):
        effect_obj = Effect(EffectsType.CUFFED)
        target_obj.effects.add(effect_obj)
        return f"{target_obj.name} is handcuffed for next turn."
    
    def release(self, target_obj):

        target_obj.effects.remove(Effect(EffectsType.CUFFED))
        return f"{target_obj.name} Is Free."
    
    def use(self,target_obj):
        return self.cuff(target_obj)

class Knife():

    def Sharp(self, shotgun_obj,dmg=2):
        effect_obj = Effect(EffectsType.Knife)
        shotgun_obj.effects.add(effect_obj)
        shotgun_obj.damage = dmg

    def resetDamage(self,shotgun_obj):
        shotgun_obj.effects.remove(Effect(EffectsType.Knife))
        shotgun_obj.damage = 1

    def use(self, shotgun_obj):

        return self.Sharp(shotgun_obj)

class Deflect():
    
    def putShield(self, shooter_obj):

        effect_obj = Effect(EffectsType.Deflect)
        shooter_obj.effects.add(effect_obj)

    
    def removeSheild(self, shooter_obj):

        shooter_obj.effects.remove(Effect(EffectsType.Deflect))

    def use(self,  shooter_obj):

        return self.putShield(shooter_obj=shooter_obj)

class Eject():
    
    def pull(self,shotgun_obj):

        shotgun_obj.shell = None
        return 1

    def use(self, shotgun_obj):
        return self.pull(shotgun_obj=shotgun_obj)

class Magnifier():
    
    def look(self, shotgun_obj):
        return shotgun_obj.shell

    def use(self,shotgun_obj):
        return self.look(shotgun_obj=shotgun_obj)

