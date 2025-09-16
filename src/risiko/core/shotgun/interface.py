from typing import Optional, Protocol, TYPE_CHECKING, runtime_checkable, Tuple
from ..magazine.interface import MagazineInterface
from ..shell.interface import ShellInterface

if TYPE_CHECKING:
    from .base import ShotgunBase

@runtime_checkable
class ShotgunInterface(Protocol):
    """Interface for a shotgun, defining its core behaviors and properties.
    Implementations should be immutable, returning new instances on state changes.
    """

    @property
    def magazine(self) -> MagazineInterface:
        """
        Returns the shotgun's magazine.
        """
        ...

    @property
    def chamber(self) -> Optional[ShellInterface]:
        """
        Returns the shell currently in the chamber, or None if empty.
        """
        ...
        
    def _load_chamber(self) -> "ShotgunBase":
        """
        Loads a shell from the magazine into the chamber.

        Returns:
            ShotgunBase: A new ShotgunBase instance with the chamber loaded.
        """
        ...
        
    
    def _unload_chamber(self) -> "ShotgunBase":
        """
        Unloads the shell from the chamber, typically back into the magazine.

        Returns:
            ShotgunBase: A new ShotgunBase instance with the chamber unloaded.
        """
        ...

    
    def _fire(self) -> Tuple[ShellInterface, "ShotgunBase"]:
        """
        Fires the shell currently in the chamber.

        Returns:
            Tuple[ShellInterface, ShotgunBase]: A tuple containing the fired shell and a new ShotgunBase instance with an empty chamber.
        """
        ...

