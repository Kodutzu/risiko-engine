from attrs import define, field

from ...core.weapon.shotgun.base import ShotgunBase
from ...core.weapon.shotgun.interface import ShotgunInterface
from ...core.weapon.shell import Shell
from .magazine import MagazineCharacter

@define
class ShotgunCharacter:

    data: ShotgunInterface = field(factory=ShotgunBase, alias="data")
    magazine: MagazineCharacter = field(factory=MagazineCharacter, alias="magazine")


    def load_chamber(self) -> Shell:

        """Loads the next shell type from the magazine into the chamber."""

        self._chamber = self.magazine.take_out_bullet()

        return self._chamber
    
    def fire(self) -> int:

        pass