from attrs import define, field,setters
from typing import Final

@define(hash=True, frozen=True)
class BlankShell:
    _damage: Final[int] = field(default=0, on_setattr=setters.frozen)

    @property
    def damage(self) -> int:
        return self._damage