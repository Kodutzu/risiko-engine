from dataclasses import dataclass
from ..Constant.Bullet import Bullet
import warnings


@dataclass
class Shell:
    _shell: int = None

    def loadInShell(self, bullet_type):
        if self._shell is not None:
            raise Exception(f"Shell already loaded with {self._shell}")
        self._shell = bullet_type
        return self._shell

    @property
    def currentShell(self):
        return self._shell
    
    @currentShell.setter
    def alterShell(self, bullet_type):

        if bullet_type in (Bullet.LIVE, Bullet.BLANK) :
            self._shell = bullet_type
        else: 
            if bullet_type is None: #To Empty!
                self._shell = bullet_type
            else:
                raise Exception(f"There's No {bullet_type}")
            
    
    def __str__(self):
        return f"Shell: {self._shell}"
