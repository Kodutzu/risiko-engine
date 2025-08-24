from ..core.shotgun.base import ShotgunBase
from ..core.shotgun.magazine import MagazineBase
from ..core.shotgun.interface import ShotgunInterface, MagazineInterface
from ..core.shotgun.snapshot import ShotgunSnapshot, MagazineSnapshot
from .interface import FactoryInterface

class ShotgunFactory(FactoryInterface):
    @staticmethod
    def assemble(
        shotgun_snapshot: ShotgunSnapshot, 
        shotgun_class: ShotgunInterface = ShotgunBase
    ) -> ShotgunInterface:
        
        return shotgun_class(
            magazine=MagazineFactory.assemble(shotgun_snapshot.magazine),
            chamber=shotgun_snapshot.chambered_shell,
            live_damage=shotgun_snapshot.live_damage,
            )
    

class MagazineFactory(FactoryInterface):

    @staticmethod
    def assemble(
        magazine_snapshot: MagazineSnapshot,
        magazine_class: MagazineInterface = MagazineBase
    ) -> MagazineInterface:
        
        return magazine_class(
            lives=magazine_snapshot.lives,
            blanks=magazine_snapshot.blanks,
            tube=magazine_snapshot.tube
        )