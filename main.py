

from GameEngine.GameObjects.Shotgun.Shotgun import Shotgun

from GameEngine.GameObjects.Constant.Bullet import Bullet

from GameEngine.GameObjects.Player.Player import Player



gun = Shotgun(lives=4, blanks=4)
player = Player(name="hello",charges=4)
print(player.charges.showCharge)

