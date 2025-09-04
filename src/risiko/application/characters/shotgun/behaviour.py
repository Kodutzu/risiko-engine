from attrs import define, field,setters
from attrs.validators import instance_of
from typing import TYPE_CHECKING
from ....core.weapon.shotgun.interface import ShotgunInterface
from ....core.weapon.shell import Shell
from ..magazine.behaviour import MagazineBehaviour

if TYPE_CHECKING:
    from .states.interface import ShotgunState


@define
class ShotgunBehaviour:

    _id: str = field(converter=str, on_setattr=setters.frozen, alias="shotgun_id")
    _data: ShotgunInterface = field(validator=instance_of(ShotgunInterface), alias="data")
    _state: "ShotgunState" = field(init=False, repr=False)
    _magazine: MagazineBehaviour = field(validator=instance_of(MagazineBehaviour), init=False)
    

    def __attrs_post_init__(self):

        self._magazine = MagazineBehaviour(data=self._data.magazine)
        
        from .states.unloaded import UnLoadedState
        self._state = UnLoadedState()

    def load_chamber(self) -> None:

        self._state.load_chamber(self)
    
    def fire(self) -> Shell:

        self._state.fire(self)

    def change_state(self, new_state: "ShotgunState") -> None:

        self._state = new_state