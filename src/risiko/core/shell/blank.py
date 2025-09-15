from attrs import define, field,setters
from typing import Final, final

@define(hash=True, frozen=True)
class BlankShell:
    """Represents a blank shell, which deals no damage."""
    _shell_type: Final[str] = field(default='blank')
    _damage: Final[int] = field(default=0)

    @property
    @final
    def damage(self) -> int:
        """
        Returns the damage dealt by the blank shell (always 0).
        """
        return self._damage
    
    
    @property
    @final 
    def shell_type(self) -> str:
        """
        Returns the type of the blank shell (always 'blank').
        """
        return self._shell_type