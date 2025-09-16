from typing import Optional, Tuple, final
from attrs import define, field, evolve
from collections import deque
from attrs.validators import instance_of, optional

from ..shell.interface import ShellInterface
from ..magazine.interface import MagazineInterface
from ..magazine.base import MagazineBase
from .exception import ShotgunLoadedException, ShotgunUnLoadedException

@define(frozen=True)
class ShotgunBase:

    """
    
    Represents the shotgun in the game, including its magazine and chamber.
    This class is immutable; all methods that modify the shotgun's state
    return a new ShotgunBase instance.

    """

    magazine: MagazineInterface = field(factory=MagazineBase,validator=instance_of(MagazineInterface))
    chamber: Optional[ShellInterface] = field(default=None, validator=optional(instance_of(ShellInterface)))

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
        new_tube = deque(self.magazine.tube)

        if self.chamber is None:

            raise ShotgunUnLoadedException("Attempted to unload, chamber is already empty")
           
        new_tube.append(self.chamber)
        return evolve(self, chamber=None, magazine=evolve(self.magazine, tube=new_tube))


    @final
    def _fire(self) -> Tuple[ShellInterface, "ShotgunBase"]:
        """
        Fires the shell currently in the chamber.

        Returns:
            Tuple[ShellInterface, ShotgunBase]: A tuple containing the fired shell and a new ShotgunBase instance with an empty chamber.

        Raises:
            ShotgunNotLoadedException: If the chamber is empty.
        """
        if self.chamber is None:

            raise ShotgunUnLoadedException()
        
        fired_shell = self.chamber


        return (fired_shell, evolve(self, chamber=None))

