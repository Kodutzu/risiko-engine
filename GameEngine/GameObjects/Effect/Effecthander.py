from ..Constant.EffectsType import EffectsType

# Improving it Overall!
# Object Error Handling!
# Pydantic Model Implementation!

class EffectHandler: # Require Error Handling - where Effect from Effecttype can be added!
    def __init__(self, effected_entity):
        self.player_effected = effected_entity #Contains all the info related to Player who has the effects
        self.effects = []

    def add(self, effect_obj):
        for effect in self.effects:
            if effect.type  == effect_obj.type:
                raise Exception(f"Effect: {effect_obj} is Already Applied")
                    
        self.effects.append(effect_obj)

    def list(self, only_active=True):
        return [
            {effect.type.name: effect.turns}
            for effect in self.effects
            if not only_active or effect.turns > 0
        ]
    
    def __contains__(self, effect_type):
        return effect_type in self.effects

    def tickAll(self):
        for effect in self.effects:
            effect.tick()

    def removeExpired(self):
        expired_effects = [effect for effect in self.effects if effect.turns <= 0]
        self.effects = [effect for effect in self.effects if effect.turns > 0]
       

