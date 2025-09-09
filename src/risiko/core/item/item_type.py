from enum import Enum, auto

class ItemType(Enum):
    CHARGER = auto() #Increase the Charge of the Player
    INVERSE = auto() #inverse the bullet - if live - then it will convert to blank - and vice versa
    HANDCUFF = auto() #Skips turns
    KNIFE = auto() #Double the damage of the next shot
    DEFLECT = auto() #Armour To The Player
    EJECT = auto() #Eject the current shell
    MAGNIFIER = auto() #See the Current shell in the magazine
    VISION = auto() #See the next shell in the magazine
    SHUFFLE = auto() #Shuffle the magazine
    BITE_THE_DUST = auto() # rewinds the game
    VOID = auto()   # Clears Player Inventory
    