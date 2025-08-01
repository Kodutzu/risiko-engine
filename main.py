from GameEngine.GameObjects.Shotgun.shotgun import Shotgun
from GameEngine.GameObjects.Constant.Bullet import Bullet
from GameEngine.GameObjects.Constant.EffectsType import EffectsType
from GameEngine.GameObjects.Effect._Effect import _Effect as Effect
from GameEngine.GameObjects.Player.Player import Player
from GameEngine.GameObjects.Loadout.Item import *

raj = Player(name="raj", charges=4)
dealer = Player(name="dealer", charges=4)
gun = Shotgun(lives=4, blanks=4)

print(gun.loadChamber())
raj.inventory.add(Knife())
raj.useItem(Knife(), raj, gun)

print(gun.effects.show())
print(raj.trigger(gun))



item_list = [Electricity, Inverse, HandCuff, Knife, Eject]



