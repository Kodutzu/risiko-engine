from enum import Enum


class EffectsType(Enum):
    CUFFED = "cuffed"
    Knife = "knife"
    Deflect = "deflect"
    ELECTRICITY = "Electricity"


class Effect:
    def __init__(self, effect_type, is_active=True):
        self.type = effect_type 
        self.is_active = is_active

    ## Adding New Instance -> True and False which can altered through Item Class!

    def Deactivate(self):
        self.is_active = False

class EffectList:
    def __init__(self, effected_entity):
        self.player_effected = effected_entity #Contains all the info related to Player who has the effects
        self.effects = []

    def add(self, effect_obj):
        for effect in self.effects:
            if effect.type  == effect_obj.type:
                raise EffectException(f"Effect: {effect_obj} is Already Applied")
                    
        self.effects.append(effect_obj)

    def has(self, effect_obj):
        for effect in self.effects:
           if effect.type == effect_obj.type:
                  return True
        return False
    
    def list(self):
       return [effect.type.name for effect in self.effects]

    def remove(self, effect_obj):
        for effect in self.effects:
            if effect.type == effect_obj.type:
                self.effects.remove(effect)
                break
    
        else:
            raise EffectException(f"Effect: {effect_obj} is not Applied")
                
        

class EffectException(Exception):
    """If The Player is Applying Item and the Effect of Item is still there - then throw an error"""
            


