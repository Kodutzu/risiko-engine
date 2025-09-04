from .interface import ShotgunState
from .....core.weapon.shell import Shell
from typing import TYPE_CHECKING, NoReturn, override

if TYPE_CHECKING:
    from ..behaviour import ShotgunBehaviour


class UnLoadedState(ShotgunState):

    @override
    def load_chamber(self, context: "ShotgunBehaviour") -> None:

        context._data.chamber = context._magazine.ejection()

        from .loaded import LoadedState
        context.change_state(LoadedState())

    @override
    def fire(self, context: "ShotgunBehaviour") -> NoReturn: 

        raise Exception("Shotgun is not loaded")
