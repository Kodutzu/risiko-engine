from risiko.application.characters.shotgun.behaviour import ShotgunBehaviour
from .interface import ShotgunState
from typing import TYPE_CHECKING, NoReturn, override

if TYPE_CHECKING:
    from ..behaviour import ShotgunBehaviour


class UnLoadedState(ShotgunState):

    @override
    def load_chamber(self, context: "ShotgunBehaviour") -> None:

        context._data.chamber = context._magazine.eject_current_shell()

        from .loaded import LoadedState
        context._change_state(LoadedState())

    @override
    def unload_chamber(self, context: ShotgunBehaviour) -> NoReturn:
        
        raise Exception("Shotgun is not loaded")

    @override
    def fire(self, context: "ShotgunBehaviour") -> NoReturn: 

        raise Exception("Shotgun is not loaded")
