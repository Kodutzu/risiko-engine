from typing import Protocol, runtime_checkable

@runtime_checkable
class ShellInterface(Protocol):
    """
    Interface for a shell, defining its damage property.
    """
    damage: int
    shell_type: str