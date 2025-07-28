from GameEngine.GameObjects.Loadout.Inventory import Inventory
from GameEngine.GameObjects.Effect.Effecthander import EffectHandler
from GameEngine.GameObjects.Constant.Bullet import Bullet

class Player:
           

    def __init__(self, name, charges=4):
        self._name = name
        self._charges = charges
        self.inventory = Inventory() 
        self.effects = EffectHandler(self)

    @property
    def charge(self):
        return self._charges
    
    def gainCharge(self, shift):
        self._charges +=shift

    def loseCharge(self,shift):
        self._charges -= shift


    @property
    def name(self):
        return self._name
    
    def trigger(self, shotgun_obj): 
        bullet = shotgun_obj.fire()

        if bullet == Bullet.LIVE:
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
        return f"Player: {self.name}, Charge: {self.charge}, Inventory: {self.inventory.show()}, Effects: {self.effects.list()}"
