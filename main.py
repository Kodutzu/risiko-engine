from GameEngine.GameObjects.Shotgun.shotgun import Shotgun
from GameEngine.GameConstant.bullet import Bullet
from GameEngine.GameConstant.item_type import ItemType
from GameEngine.GameObjects.Effect._effect import _Effect as Effect
from GameEngine.GameObjects.Player.player import Player
from GameEngine.GameObjects.Loadout.item import *

raj = Player(name="raj", charges=4)
dealer = Player(name="dealer", charges=4)
gun = Shotgun(lives=4, blanks=4)

print(gun.loadChamber())
raj.inventory.add(Knife())
data = raj.useItem(Knife(), raj, gun)

print(data.item_applied.damage)

print(gun.effects.show())
print(raj.trigger(gun))
gun.effects.tickAll()
gun.effects.removeExpired()
print(gun.effects.show(only_active=False))



item_list = [Electricity, Inverse, HandCuff, Knife, Eject]



