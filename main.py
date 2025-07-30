

from GameEngine.GameObjects.Shotgun.Shotgun import Shotgun

from GameEngine.GameObjects.Constant.Bullet import Bullet
from GameEngine.GameObjects.Constant.EffectsType import EffectsType

from GameEngine.GameObjects.Effect.Effect import _Effect as Effect
from GameEngine.GameObjects.Player.Player import Player

from GameEngine.GameObjects.Loadout.Item import *


raj = Player(name="Raj", charges=4)
dealer = Player(name="dealer", charges=4)
gun = Shotgun(lives=4, blanks=4)


gun.loadChamber()
raj.inventory.add([Electricity(), Eject(), Magnifier()])
dealer.inventory.add([Knife(), Electricity(), HandCuff()])


print(gun.shell.currentShell)
bullet = raj.trigger(gun)

print(bullet)

if(bullet == 1):
    dealer.charges.lose(gun.liveDamage)

dealer.useItem(Electricity(),dealer,dealer )
dealer.useItem(HandCuff(), dealer, raj)
dealer.useItem(Knife(), dealer, gun)

gun.loadChamber()

print(gun.shell.currentShell)
print(gun.liveDamage)
damage = dealer.trigger(gun)
raj.charges.lose(damage)


print(raj)
print(gun)
print(dealer)


