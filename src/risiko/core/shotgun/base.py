from typing import Optional, Tuple, final, override

from attrs import define, evolve, field

from ..magazine import MagazineBase, MagazineInterface
from ..shell.interface import ShellInterface
from .exception import ShotgunLoadedException, ShotgunUnLoadedException
from .interface import ShotgunInterface


@define(frozen=True)
class ShotgunBase(ShotgunInterface):
    """
    Represents the shotgun in the game, including its magazine and chamber.
    This class is immutable; all methods that modify the shotgun's state
    return a new ShotgunBase instance.
    """

    magazine: MagazineInterface = field(factory=MagazineBase, kw_only=True)
    chamber: Optional[ShellInterface] = field(default=None, kw_only=True)

    @final
    @override
    def load_chamber(self) -> "ShotgunBase":
        """
        Loads a shell from the magazine into the chamber.

        Returns:
            ShotgunBase: A new ShotgunBase instance with the chamber loaded and magazine updated.

        Raises:
            ShotgunLoadedException: If the chamber is already loaded.
        """

        if self.chamber is not None:
            raise ShotgunLoadedException("Shotgun is Already Loaded")

        new_chamber, new_magazine = self.magazine.eject_shell()

        return evolve(self, chamber=new_chamber, magazine=new_magazine)

    @final
    @override
    def unload_chamber(self) -> "ShotgunBase":
        """
        Unloads the shell from the chamber back into the magazine.

        Returns:
            ShotgunBase: A new ShotgunBase instance with the chamber empty and magazine updated.

        Raises:
            ShotgunUnLoadedException: If the chamber is already empty.
        """
        if self.chamber is None:
            raise ShotgunUnLoadedException(
                "Attempted to unload, chamber is already empty"
            )

        new_magazine = self.magazine.load_round([self.chamber])
        return evolve(self, chamber=None, magazine=new_magazine)

    @final
    @override
    def fire(self) -> Tuple[ShellInterface, "ShotgunBase"]:
        """
        Fires the shell currently in the chamber.

        Returns:
            Tuple[ShellTypeT, ShotgunBase]: A tuple containing the fired shell and a new ShotgunBase instance with an empty chamber.

        Raises:
            ShotgunUnLoadedException: If the chamber is empty.
        """
        if self.chamber is None:
            raise ShotgunUnLoadedException(
                message="Attempted to fire, chamber is empty (Not Loaded)"
            )

        fired_shell = self.chamber

        return (fired_shell, evolve(self, chamber=None))
