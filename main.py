from GameEngine.GameObjects.Shotgun.shotgun import Shotgun
from GameEngine.GameConstant.bullet import Bullet
from GameEngine.GameConstant.item_type import ItemType
from GameEngine.GameObjects.Effect._effect import _Effect as Effect
from GameEngine.GameObjects.Player.player import Player
from GameEngine.GameObjects.Loadout.item import *

raj = Player(name="raj", charges=4)
dealer = Player(name="dealer", charges=4)
gun = Shotgun(lives=4, blanks=4)

print(raj.name)

# gun.loadChamber()
# raj.inventory.add([Electricity(), Magnifier(), Vision(), HandCuff()])
# raj.useItem(Magnifier(), raj, gun)
# raj.useItem(Electricity(), raj, raj)
# data = raj.useItem(HandCuff(), raj,dealer)

# print(data.item_applied.effects_applied)

# print(raj.charges.showCharge)
# print(gun.magazine.getMagazine())



# item_list = [Electricity, Inverse, HandCuff, Knife, Eject]



