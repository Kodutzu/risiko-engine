

from GameEngine.GameObjects.Shotgun.Shotgun import Shotgun

from GameEngine.GameObjects.Constant.Bullet import Bullet
from GameEngine.GameObjects.Constant.EffectsType import EffectsType

from GameEngine.GameObjects.Effect.Effect import _Effect as Effect
from GameEngine.GameObjects.Player.Player import Player
import warnings
from GameEngine.GameObjects.Loadout.Item import *
warnings.simplefilter("always", DeprecationWarning)


gun = Shotgun()
player = Player(name="byebye",charges=10)

print(gun.magazine.getMagazine)

player.inventory.add([HandCuff(), Knife(), Electricity()])
gun.loadChamber()
print(gun.shell.currentShell)
print(player.trigger(shotgun_obj=gun))

