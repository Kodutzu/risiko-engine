from typing import Protocol, runtime_checkable, TYPE_CHECKING, Tuple, Iterable
from ..shell import ShellInterface

if TYPE_CHECKING:
    pass

@runtime_checkable
class MagazineInterface(Protocol):
    """
    Interface for a magazine, defining its core behaviors and properties.
    Implementations should be immutable, returning new instances on state changes.
    """

    @property
    def tube(self) -> Tuple[ShellInterface, ...]:
        """
        Returns the deque of shells currently in the magazine tube.
        """
        ...


    def _load_round(self, shells: Iterable[ShellInterface]) -> "MagazineInterface":
        """
        Loads a new round of shells into the magazine.

        Args:
            shells (Iterable[ShellType]): A collection of shell objects to add to the magazine.

        Returns:
            MagazineInterface[ShellType]: A new magazine instance with the loaded shells.
        """
        ...

    def _eject_shell(self) -> Tuple[ShellInterface, "MagazineInterface"]:
        """
        Ejects the first shell from the magazine.

        Returns:
            Tuple[ShellType, MagazineInterface[ShellType]]: A tuple containing the ejected shell and a new magazine instance.
        """
        ...

    def _clear(self) -> "MagazineInterface":
        """
        Clears all shells from the magazine.

        Returns:
            MagazineInterface[ShellType]: A new magazine instance with an empty magazine.
        """
        ...


     


