from .interface import ShotgunState
from .....core.weapon.shell import Shell
from typing import TYPE_CHECKING, NoReturn, override, Optional

if TYPE_CHECKING:
    from ..behaviour import ShotgunBehaviour


class LoadedState(ShotgunState):

    
    @override
    def load_chamber(self, context: "ShotgunBehaviour") -> NoReturn:

        raise Exception("Shotgun is already loaded")

    @override
    def fire(self, context: "ShotgunBehaviour") -> Optional[Shell]: 

        fired_shell = context._data.chamber

        context._data.chamber = None

        from .unloaded import UnLoadedState
        context.change_state(UnLoadedState())

        return fired_shell
