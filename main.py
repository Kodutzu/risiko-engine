from BuckShot.GameObjects.Player.player import Player
from BuckShot.GameObjects.Shotgun.shotgun import Shotgun
from BuckShot.GameConstant.bullet import Bullet
from BuckShot.GameObjects.Loadout.item import Item
from BuckShot.GameConstant.usable_entity import UsableEntity


gun = Shotgun(lives=4, blanks=4)

print(gun.magazine.getMagazine())

gun.loadChamber()
print(type(gun.shell.currentShell.name))
player = Player(id=1, charges=4)
player.inventory.add(Item(type_of=UsableEntity.CUFFED))
# print(player.inventory.show(readable=True))


