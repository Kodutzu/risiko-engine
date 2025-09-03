from attrs import define, field

from ....core.weapon.shotgun.interface import ShotgunInterface
from ....core.weapon.shell import Shell
from ..magazine.behaviour import MagazineBehaviour

@define
class ShotgunBehaviour:

    data: ShotgunInterface = field( alias="data")
    magazine: MagazineBehaviour = field(factory=MagazineBehaviour, alias="magazine")


    def load_chamber(self) -> Shell:

        """Loads the next shell type from the magazine into the chamber."""

        self._chamber = self.magazine.take_out_bullet()

        return self._chamber
    
    def fire(self) -> int:

        pass