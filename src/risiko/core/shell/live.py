from attrs import define, field,setters
from attrs.validators import ge
from typing import Final

@define(hash=True, frozen=True)
class LiveShell:

    _damage: Final[int] = field(default=1, on_setattr=setters.frozen)

    @property
    def damage(self) -> int:
        return self._damage