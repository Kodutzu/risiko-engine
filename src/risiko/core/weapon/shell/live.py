from attrs import define, field,setters
from attrs.validators import ge
from typing import Final

@define(hash=True)
class LiveShell:

    _damage: int = field(default=1)

    @property
    def damage(self) -> int:
        return self._damage

 