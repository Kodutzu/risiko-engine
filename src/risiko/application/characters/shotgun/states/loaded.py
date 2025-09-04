from .interface import ShotgunState
from .....core.weapon.shell import Shell
from typing import TYPE_CHECKING, NoReturn

if TYPE_CHECKING:
    from ..behaviour import ShotgunBehaviour


class LoadedState(ShotgunState):

    
    def load_chamber(self, context: "ShotgunBehaviour") -> NoReturn:

        raise Exception("Shotgun is already loaded")

    def fire(self, context: "ShotgunBehaviour") -> Shell: 

        fired_shell = context._data.chamber

        context._data.chamber = None

        from .unloaded import UnLoadedState
        context.change_state(UnLoadedState())

        return fired_shell
