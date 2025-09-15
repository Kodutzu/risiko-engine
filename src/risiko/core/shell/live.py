from attrs import define, field, setters
from typing import Final, final

@define(hash=True, frozen=True)
class LiveShell:
    """Represents a live shell, which deals damage."""
    _shell_type: Final[str] = field(default='live')
    _damage: Final[int] = field(default=1)

    @property
    @final
    def damage(self) -> int:
        """
        Returns the damage dealt by the live shell (default 1).
        """
        return self._damage

    @property
    @final 
    def shell_type(self) -> str:
        """
        Returns the type of the live shell (always 'live').
        """
        return self._shell_type