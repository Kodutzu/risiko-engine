from .interface import ShellInterface
from attrs import define, field


@define
class BlankShell(ShellInterface):
    _damage: int = field(default=0)

    @property
    def damage(self) -> int:
        return self._damage