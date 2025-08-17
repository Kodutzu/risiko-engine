from pydantic import BaseModel, PrivateAttr
from ..constant.bullet import Bullet
from ..exception.shotugn_exception import ShellException

class Shell(BaseModel):
    
    _shell: Bullet | None = PrivateAttr(default=None)

    def load(self, bullet_type:Bullet) -> Bullet:
        """
        Loads a shell into the shotgun.
        Raises a ShellException if the shell is already loaded.
        """
        if self._shell is not None:
            raise ShellException(f"Shell already loaded with {self._shell}")
        
        self._shell = bullet_type
        return self._shell
    
    def unload(self) -> Bullet:
        """
        Unloads the shell from the shotgun.
        Returns the unloaded shell.
        """
        old_shell = self._shell
        self._shell = None
        return old_shell
    
    def isLoaded(self) -> bool: 
        """
        Checks if the shell is loaded.
        """
        return self._shell is not None
    
    @property
    def currentShell(self) -> Bullet:
        """
        Returns the currently loaded shell.
        """
        return self._shell
    
    def __str__(self):
        return f"Shell: {self._shell}"
    
