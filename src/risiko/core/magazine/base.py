from collections import deque
from typing import Deque, Iterable, Tuple, final, override

from attrs import define, evolve, field

from ..shell import ShellInterface
from .exception import MagazineEmptyException
from .interface import MagazineInterface


@define(frozen=True)
class MagazineBase(MagazineInterface):
    """Represents the shotgun's magazine, holding a deque of shells.
    This class is immutable; all methods that modify the magazine's state
    return a new MagazineBase instance.
    """

    _tube: Deque[ShellInterface] = field(factory=deque, alias="tube", kw_only=True)

    @property
    @final
    @override
    def tube(self) -> Tuple[ShellInterface, ...]:
        return tuple(self._tube)

    @final
    @override
    def load_round(self, shells: Iterable[ShellInterface]) -> "MagazineBase":
        """
        Loads a list of shell objects into the magazine.

        Args:
            shells (Iterable[ShellInterface]): A list of shell objects to add to the magazine.

        Returns:
            MagazineBase: A new MagazineBase instance with the added shells.
        """

        new_tube = self._tube.copy()
        new_tube.extend(shells)

        return evolve(self, tube=new_tube)

    @final
    @override
    def eject_shell(self) -> Tuple[ShellInterface, "MagazineBase"]:
        """
        Ejects the first shell from the magazine.

        Returns:
            Tuple[ShellType, MagazineBase]: A tuple containing the ejected shell and a new MagazineBase instance.

        Raises:
            MagazineEmptyException: If the magazine is empty.
        """
        if not self.tube:
            raise MagazineEmptyException(info="Failed to Eject Shell")

        new_tube = self._tube.copy()

        shell = new_tube.popleft()

        return (shell, evolve(self, tube=new_tube))

    @final
    @override
    def clear(self) -> "MagazineBase":
        """
        Clears all shells from the magazine.

        Returns:
            MagazineBase: A new MagazineBase instance with an empty magazine.

        Raises:
            MagazineEmptyException: If the magazine is already empty.
        """
        if not self.tube:
            raise MagazineEmptyException(info="failed to clear magazine")

        new_tube = self._tube.copy()
        new_tube.clear()

        return evolve(self, tube=new_tube)
