from typing import Optional, Tuple, final
from attrs import define, field, evolve

from ..shell.interface import ShellInterface
from .interface import ShotgunInterface
from ..magazine import MagazineInterface, MagazineBase
from .interface import ShotgunInterface # Added import
from .exception import ShotgunLoadedException, ShotgunUnLoadedException

@define(frozen=True)
class ShotgunBase(ShotgunInterface):
    """
    Represents the shotgun in the game, including its magazine and chamber.
    This class is immutable; all methods that modify the shotgun's state
    return a new ShotgunBase instance.
    """

    magazine: MagazineInterface = field(factory=MagazineBase)
    chamber: Optional[ShellInterface] = field(default=None)

    @final
    def _load_chamber(self) -> "ShotgunBase":
        """
        Loads a shell from the magazine into the chamber.

        Returns:
            ShotgunBase: A new ShotgunBase instance with the chamber loaded and magazine updated.

        Raises:
            ShotgunLoadedException: If the chamber is already loaded.
        """
        
        if self.chamber is not None:
            raise ShotgunLoadedException("Shotgun is Already Loaded")
        
        new_chamber, new_magazine = self.magazine._eject_shell()

        return evolve(self, chamber=new_chamber, magazine=new_magazine)
    

    @final
    def _unload_chamber(self) -> "ShotgunBase":
        """
        Unloads the shell from the chamber back into the magazine.

        Returns:
            ShotgunBase: A new ShotgunBase instance with the chamber empty and magazine updated.

        Raises:
            ShotgunUnLoadedException: If the chamber is already empty.
        """
        if self.chamber is None:
            raise ShotgunUnLoadedException("Attempted to unload, chamber is already empty")
        
        # Refactored to use the interface method, removing dependency on concrete MagazineBase
        new_magazine = self.magazine._load_round([self.chamber])
        return evolve(self, chamber=None, magazine=new_magazine)


    @final
    def _fire(self) -> Tuple[ShellInterface, "ShotgunBase"]:
        """
        Fires the shell currently in the chamber.

        Returns:
            Tuple[ShellTypeT, ShotgunBase]: A tuple containing the fired shell and a new ShotgunBase instance with an empty chamber.

        Raises:
            ShotgunNotLoadedException: If the chamber is empty.
        """
        if self.chamber is None:
            raise ShotgunUnLoadedException()
        
        fired_shell = self.chamber

        return (fired_shell, evolve(self, chamber=None))

