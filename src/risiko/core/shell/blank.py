from attrs import define, field,setters
from typing import Final, final

@define(hash=True, frozen=True)
class BlankShell:
    """Represents a blank shell, which deals no damage."""
    _damage: Final[int] = field(default=0)

    @property
    @final
    def damage(self) -> int:
        """
        Returns the damage dealt by the blank shell (always 0).
        """
        return self._damage