from attrs import define, field, setters
from typing import Final, final

@define(hash=True, frozen=True)
class LiveShell:
    """Represents a live shell, which deals damage."""

    _damage: Final[int] = field(default=1)

    @property
    @final
    def damage(self) -> int:
        """
        Returns the damage dealt by the live shell (default 1).
        """
        return self._damage