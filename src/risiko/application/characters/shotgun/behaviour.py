from attrs import define, field,setters, Factory
from attrs.validators import instance_of
from typing import TYPE_CHECKING


from ....core.weapon.shotgun.interface import ShotgunInterface
from ..magazine.behaviour import MagazineBehaviour

if TYPE_CHECKING:
    from .states.interface import ShotgunState


@define
class ShotgunBehaviour:

    magazine_behaviour: MagazineBehaviour = field(validator=instance_of(MagazineBehaviour), init=False)
    _data: ShotgunInterface = field(validator=instance_of(ShotgunInterface), alias="shotgun_base")
    _state: "ShotgunState" = field(init=False, repr=False)

    def __attrs_post_init__(self):

        self.magazine_behaviour = MagazineBehaviour(magazine_base=self._data.magazine)
        
        from .states.unloaded import UnLoadedState
        self._state = UnLoadedState()

    @property
    def id(self) -> str:
        return self._data.id
    
    def load_chamber(self) -> None:

        self._state.load_chamber(context=self)

    def unload_chamber(self) -> None:

        self._state.unload_chamber(context=self)
    
    def fire(self) -> None:

        self._state.fire(context=self)

    def _change_state(self, new_state: "ShotgunState") -> None:

        self._state = new_state