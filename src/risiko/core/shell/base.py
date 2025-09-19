from attrs import define, field
from attrs.validators import ge

from .interface import ShellInterface

@define(frozen=True)
class ShellBase(ShellInterface):
    """Represents a generic shell with configurable properties."""
    shell_type: str 
    damage: int = field(validator=ge(0))

