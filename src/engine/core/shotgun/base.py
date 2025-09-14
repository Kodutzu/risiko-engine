from typing import Optional, Tuple, final
from attrs import define, field, evolve
from attrs.validators import instance_of

from ..shell.interface import ShellInterface
from ..magazine.interface import MagazineInterface
from ..magazine.base import MagazineBase
from .exception import ShotgunNotLoadedException

@define(frozen=True)
class ShotgunBase:

    """
    
    Represents the shotgun in the game, including its magazine and chamber.
    This class is immutable; all methods that modify the shotgun's state
    return a new ShotgunBase instance.

    """

    magazine: MagazineInterface = field(factory=MagazineBase,validator=instance_of(MagazineInterface))
    chamber: Optional[ShellInterface] = field(default=None, validator=instance_of((ShellInterface, type(None))))

    @final
    def load_chamber(self) -> "ShotgunBase":
        """
        Loads a shell from the magazine into the chamber.

        Returns:
            ShotgunBase: A new ShotgunBase instance with the chamber loaded and magazine updated.
        """
      
        new_chamber, new_magazine = self.magazine.eject_shell()

        return evolve(self, chamber=new_chamber, magazine=new_magazine)

    @final
    def unload_chamber(self) -> "ShotgunBase":
        """
        Unloads the shell from the chamber back into the magazine.

        Returns:
            ShotgunBase: A new ShotgunBase instance with the chamber empty and magazine updated.

        Raises:
            ShotgunNotLoadedException: If the chamber is already empty.
        """
        new_tube = self.magazine.tube.copy()

        if self.chamber is None:

            raise ShotgunNotLoadedException("Attempted to unload, chamber is already empty")
           
        new_tube.append(self.chamber)
        return evolve(self, chamber=None, magazine=evolve(self.magazine, tube=new_tube))


    @final
    def fire(self) -> Tuple[ShellInterface, "ShotgunBase"]:
        """
        Fires the shell currently in the chamber.

        Returns:
            Tuple[ShellInterface, ShotgunBase]: A tuple containing the fired shell and a new ShotgunBase instance with an empty chamber.

        Raises:
            ShotgunNotLoadedException: If the chamber is empty.
        """
        if self.chamber is None:

            raise ShotgunNotLoadedException()
        
        fired_shell = self.chamber


        return (fired_shell, evolve(self, chamber=None))

