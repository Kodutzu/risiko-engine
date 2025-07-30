from pydantic import BaseModel, PrivateAttr
from ..Constant.Bullet import Bullet
import warnings


class _Shell(BaseModel):
    _shell: Bullet| None = PrivateAttr(default=None)

    def loadShell(self, bullet_type):
        if self._shell is not None:
            raise Exception(f"Shell already loaded with {self._shell}")
        self._shell = bullet_type
        return self._shell
    
    def isLoaded(self) -> bool: 
        return self._shell is not None

    def unloadShell(self):
        self._shell = None

    @property
    def currentShell(self) -> Bullet:
        return self._shell
    

    def __str__(self):
        return f"Shell: {self._shell}"
