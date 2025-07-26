from Game_Mechanics.GameObjects.Inventory import Inventory
from Game_Mechanics.GameObjects.Effect import Effect, EffectsType, EffectList

class Player:
            

    def __init__(self, name, charges=4):
        self._name = name
        self._charges = charges
        self.inventory = Inventory() 
        self.effects = EffectList(self)

    @property
    def charge(self):
        return self._charges
    
    @charge.setter
    def charge(self, chargeShift ):
       
        if chargeShift >= 0:
           self._charges +=chargeShift

        elif chargeShift <0:
            self._charges +=chargeShift #It will end-up Subtracting -> (-)(+) = (-)

        else:
            pass


    @property
    def name(self):
        return self._name
    
    def shoot(self, shotgun_obj):
        
        return shotgun_obj.Fire()


    def useItem(self, item_obj, entity):
        if not self.inventory.hasItem(item_obj):
            raise InvalidItemException("This Item Doesn't Exist")
        
        return item_obj.use(entity)


class InvalidItemException(Exception):
    """When The Item is not present in the inventory"""

