from attrs import define

@define(frozen=True)
class ShellBase:
    """Represents a generic shell with configurable properties."""
    shell_type: str 
    damage: int = 0

