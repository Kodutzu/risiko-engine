from attrs import define, field
from attrs.validators import instance_of
from ....core.weapon.shotgun.interface import ShotgunInterface
from ....core.weapon.shell import Shell
from ..magazine.behaviour import MagazineBehaviour

@define
class ShotgunBehaviour:

    _data: ShotgunInterface = field(validator=instance_of(ShotgunInterface), alias="data")
    magazine: MagazineBehaviour = field(validator=instance_of(MagazineBehaviour),factory=MagazineBehaviour)


    def load_chamber(self) -> Shell:

        """Loads the next shell type from the magazine into the chamber."""

        self._chamber = self.magazine.take_out_bullet()

        return self._chamber
    
    def fire(self) -> int:

        pass