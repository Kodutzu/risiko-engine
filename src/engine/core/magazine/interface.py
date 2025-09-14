from typing import Deque, Protocol,runtime_checkable, TYPE_CHECKING, Tuple
from ..shell.interface import ShellInterface

if TYPE_CHECKING:
    from .base import MagazineBase

@runtime_checkable
class MagazineInterface(Protocol):
    """
    Interface for a magazine, defining its core behaviors and properties.
    Implementations should be immutable, returning new instances on state changes.
    """

    @property
    def tube(self) ->  Deque[ShellInterface]:
        """
        Returns the deque of shells currently in the magazine tube.
        """
        ...
    
    @property
    def is_empty(self) ->  bool:
        """
        Checks if the magazine is empty.
        """
        ...

    def load_round(self,lives:int, blanks:int) -> "MagazineBase":
        """
        Loads a new round of shells into the magazine.

        Args:
            lives (int): The number of live shells to add.
            blanks (int): The number of blank shells to add.

        Returns:
            MagazineBase: A new MagazineBase instance with the loaded shells.
        """
        ...
    
    def eject_shell(self) -> Tuple[ShellInterface, "MagazineBase"]:

        """
        Ejects the first shell from the magazine.

        Returns:
            Tuple[ShellInterface, MagazineBase]: A tuple containing the ejected shell and a new MagazineBase instance.
        """
        ...
    
    def clear(self) -> "MagazineBase":

        """
        Clears all shells from the magazine.

        Returns:
            MagazineBase: A new MagazineBase instance with an empty magazine.
        """
        
        ...


     


