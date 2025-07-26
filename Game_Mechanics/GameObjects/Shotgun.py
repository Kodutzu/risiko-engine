from Game_Mechanics.GameObjects.Effect import EffectList
import random



class Shotgun:

    def __init__(self,lives=4, blanks=4,stuns=1):

        self.base_magazine = {
            "LIVE": lives,
            "BLANK": blanks,
            "STUN": stuns
        }

        self.increment = {
            "LIVE": 2,
            "BLANK": 1
        }

        self.magazine = self.base_magazine.copy()
        self._shell = None
        self._dmg = 1
        self.effects = EffectList(self)

    @property
    def shell(self):
        return self._shell
    
    @property
    def damage(self):
        return self._dmg
    

    def loadShell(self):

        available_bullets = [bullets for bullets, count in self.magazine.items() if count > 0 ]

        if (("LIVE" not in available_bullets )or ("BLANK" not in available_bullets)):
            raise EmptyMagazineException("Ran out of Bullets - Please Reload")
            # New Gamestate - New round in a level

        else:
            
            self._shell =random.choice(available_bullets)
            self.magazine[self.shell] -= 1
            
    @shell.setter
    def shell(self, opp_shell):
        if(opp_shell not in ["LIVE", "BLANK", "STUN", None]):
            raise ValueError("Wrong Input of Bullets")
        self._shell = opp_shell
        return self._shell
    
    @damage.setter
    def damage(self,new_dmg):
        if(new_dmg <=0):
            raise ValueError("Damage Can't be Zero or less")
        
        self._dmg = new_dmg

        return self._dmg


    def ReloadMagazine(self):
        
        self.base_magazine["LIVE"] += self.increment["LIVE"]
        self.base_magazine["BLANK"] += self.increment["BLANK"]
        self.magazine = self.base_magazine.copy()

    def Fire(self):

        if(self._shell == None):
            raise EmptyShellException("Bullet is not Loaded, Please Load it first")

        self.load = self.shell
        self._shell = None
        return self.load
    
        
class EmptyShellException(Exception):
    """Raised when attempting to shoot without loading a shell."""
    pass

class EmptyMagazineException(Exception):
    """Raised when Either LIVE or BLANK are Used Up."""
    pass

    


        
    

        


        