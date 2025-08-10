from GameEngine.GameObjects.Player.player import Player
from GameEngine.GameObjects.Shotgun.shotgun import Shotgun
from GameEngine.GameObjects.Loadout.Item import *
from GameEngine.GameObjects.Effect._effect import _Effect as Effect
from GameEngine.GameConstant.item_type import ItemType


gun = Shotgun()
player = Player(id=1101, charges=4, _inventory=gun, effects=gun.effects)

player.inventory.add(Electricity())
player.effects.add(Effect(ItemType.ELECTRICITY))
print(player)

print(gun.magazine.getMagazine(as_list=True))