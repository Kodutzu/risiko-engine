from risiko.application.characters.shotgun.behaviour import ShotgunBehaviour
from .interface import ShotgunState
from .....core.weapon.shell.interface import ShellInterface
from typing import TYPE_CHECKING, NoReturn, override, Optional, Type

if TYPE_CHECKING:
    from ..behaviour import ShotgunBehaviour


class LoadedState(ShotgunState):

    
    @override
    def load_chamber(self, context: "ShotgunBehaviour") -> NoReturn:

        raise Exception("Shotgun is already loaded")
    
    @override
    def unload_chamber(self, context: ShotgunBehaviour) -> None:

        if isinstance(context._data.chamber,ShellInterface):
            context.magazine_behaviour._data.tube.appendleft(context._data.chamber)

        context._data.chamber = None

        from .unloaded import UnLoadedState
        context._change_state(UnLoadedState())

    @override
    def fire(self, context: "ShotgunBehaviour") -> ShellInterface: 


        if not isinstance(context._data.chamber,ShellInterface):

            from .unloaded import UnLoadedState
            context._change_state(UnLoadedState())
            raise Exception("Shotgun is not loaded")

        fired_shell = context._data.chamber
        context._data.chamber = None

        from .unloaded import UnLoadedState
        context._change_state(UnLoadedState())

        return fired_shell
