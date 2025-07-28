from GameEngine.GameObjects.Loadout.Inventory import Inventory
from GameEngine.GameObjects.Effect.Effecthander import EffectHandler
from GameEngine.GameObjects.Constant.Bullet import Bullet
from dataclasses import dataclass

class Player:
           
    def __init__(self, name, charges=4):
        self._name = name
        self.charges = _ChargeMeter(charges)
        self.inventory = Inventory() 
        self.effects = EffectHandler(self)

    @property
    def name(self):
        return self._name
    
    def trigger(self, shotgun_obj): 
        bullet = shotgun_obj.fire()

        if bullet == 1:
            return 1 #return more 
        else: 
            return 0

    def useItem(self, item_obj, entity_obj):

        if not self.inventory.has(item_obj):
            raise Exception("This Item Doesn't Exist")
        
        self.usage = item_obj.use(entity_obj)
        self.inventory.remove(item_obj)
        return self.usage

    def __str__(self):
        return f"Player: {self.name}, Charge: {self.showCharges}, Inventory: {self.inventory.show()}, Effects: {self.effects.list()}"

@dataclass
class _ChargeMeter:
    value: int = 4

    def gain(self, amt): self.value +=amt
    def lose(self,amt): self.value -=amt
    @property
    def showCharge(self): return self.value
    def __int__(self): return self.value
