from attrs import define, field, evolve
from attrs.validators import instance_of
from typing import Deque, final, Tuple, Iterable
from collections import deque


from ..shell import ShellInterface
from .exception import MagazineEmptyException

@define(frozen=True)
class MagazineBase:
    """Represents the shotgun's magazine, holding a deque of shells.
    This class is immutable; all methods that modify the magazine's state
    return a new MagazineBase instance.
    """
     
    _tube: Deque[ShellInterface] = field(factory=deque, validator=instance_of(deque))

    @property
    @final
    def tube(self) ->  Tuple[ShellInterface, ...]:
        return tuple(self._tube)
    
    @property
    @final
    def is_empty(self) -> bool:
        """
        Checks if the magazine is empty.

        Returns:
            bool: True if the magazine is empty, False otherwise.
        """
        return not self._tube

    
    @final
    def _load_round(self, shells: Iterable[ShellInterface]) -> "MagazineBase":
        """
        Loads a list of shell objects into the magazine.

        Args:
            shells (List[ShellInterface]): A list of shell objects to add to the magazine.

        Returns:
            MagazineBase: A new MagazineBase instance with the added shells.
        
        Raises:
            MagazineFullException: If the magazine is or becomes full during the operation.
        """

        new_tube = self._tube.copy()
        new_tube.extend(shells)

        return evolve(self, tube=new_tube)
    
    @final
    def _eject_shell(self) -> Tuple[ShellInterface, "MagazineBase"]:
        """
        Ejects the first shell from the magazine.

        Returns:
            Tuple[ShellInterface, MagazineBase]: A tuple containing the ejected shell and a new MagazineBase instance.

        Raises:
            MagazineEmptyException: If the magazine is empty.
        """
        if self.is_empty:

            raise MagazineEmptyException()

        new_tube = self._tube.copy()

        shell = new_tube.popleft()
            
        return (shell, evolve(self, tube=new_tube))
    
    @final
    def _clear(self) -> "MagazineBase":
        """
        Clears all shells from the magazine.

        Returns:
            MagazineBase: A new MagazineBase instance with an empty magazine.

        Raises:
            MagazineEmptyException: If the magazine is already empty.
        """
        if self.is_empty:
            
            raise MagazineEmptyException("Magazine is already Empty")

        new_tube = self._tube.copy()
        new_tube.clear()

        return evolve(self, tube=new_tube)


     


    
