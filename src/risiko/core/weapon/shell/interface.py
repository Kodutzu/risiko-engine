from typing import Protocol, runtime_checkable

@runtime_checkable
class ShellInterface(Protocol):

    @property
    def damage(self) -> int:
        ...