from attrs import define, field
from attrs.validators import ge, instance_of

from .interface import ShellInterface


@define(frozen=True)
class ShellBase(ShellInterface):
    """Represents a generic shell with configurable properties."""

    shell_type: str = field(kw_only=True, validator=instance_of(str))
    damage: int = field(validator=(ge(0), instance_of(int)), kw_only=True)
