from attrs import define, field
from attrs.validators import ge

from .interface import ShellInterface

@define(frozen=True)
class ShellBase(ShellInterface):
    """Represents a generic shell with configurable properties."""
    shell_type: str =field(kw_only=True)
    damage: int = field(validator=ge(0), kw_only=True)

