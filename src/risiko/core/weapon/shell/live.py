from .interface import ShellInterface
from attrs import define, field


@define
class LiveShell(ShellInterface):
    _damage: int = field(default=1)

    @property
    def damage(self) -> int:
        return self._damage