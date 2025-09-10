from attrs import define, field
from typing import Final

@define(hash=True)
class BlankShell:
    _damage: Final[int] = field(default=0)

    @property
    def damage(self) -> int:
        return self._damage