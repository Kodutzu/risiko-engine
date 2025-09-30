from typing import Optional, Protocol, Tuple, runtime_checkable

from ..magazine.interface import MagazineInterface
from ..shell.interface import ShellInterface


@runtime_checkable
class ShotgunInterface(Protocol):
    """Interface for a shotgun, defining its core behaviors and properties.
    Implementations should be immutable, returning new instances on state changes.
    """

    magazine: MagazineInterface
    chamber: Optional[ShellInterface]

    def load_chamber(self) -> "ShotgunInterface":
        """
        Loads a shell from the magazine into the chamber.

        Returns:
            ShotgunInterface: A new shotgun instance with the chamber loaded.
        """
        ...

    def unload_chamber(self) -> "ShotgunInterface":
        """
        Unloads the shell from the chamber, typically back into the magazine.

        Returns:
            ShotgunInterface: A new shotgun instance with the chamber unloaded.
        """
        ...

    def fire(self) -> Tuple[ShellInterface, "ShotgunInterface"]:
        """
        Fires the shell currently in the chamber.

        Returns:
            Tuple[ShellInterface, ShotgunInterface]: A tuple containing the fired shell and a new shotgun instance with an empty chamber.
        """
        ...
