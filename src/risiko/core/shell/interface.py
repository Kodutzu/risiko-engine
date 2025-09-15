from typing import Protocol, runtime_checkable

@runtime_checkable
class ShellInterface(Protocol):
    """
    Interface for a shell, defining its damage property.
    """

    @property
    def damage(self) -> int:
        """
        Returns the damage value of the shell.
        """
        ...
    @property
    def shell_type(self) -> str:
        """
        Returns the type of the shell.
        """
        ...