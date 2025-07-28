

from GameEngine.GameObjects.Shotgun.Shotgun import Shotgun
from GameEngine.GameObjects.Constant.Bullet import Bullet
from GameEngine.GameObjects.Shotgun._Magazine import Magazine


gun = Shotgun(lives=4, blanks=4)

gun.loadChamber()
gun.liveDamage = 2

gun.shell.alterShell=None
print(gun.shell.currentShell)


print(gun.magazine.getMagazine)

