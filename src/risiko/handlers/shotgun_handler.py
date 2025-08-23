from ..core.shotgun.base import ShotgunBase
from ..core.shotgun.magazine import MagazineBase
from ..core.shotgun.snapshot import ShotgunSnapshot, MagazineSnapshot
from ..core.shotgun.interface import ShotgunInterface, MagazineInterface
from ..core.game.snapshot import GameSnapshot
from ..constants.shell import Shell
from typing import Union

class ShotgunFactory: # Currenlty Hard Coded for BaseClasses
    @staticmethod
    def create_shotgun(shotgun_snapshot: ShotgunSnapshot) -> Union[ShotgunInterface, ShotgunBase]:
        return ShotgunBase(
            magazine=ShotgunFactory.create_magazine(shotgun_snapshot.magazine),
            _chamber=shotgun_snapshot.chambered_shell,
            _live_dmg=shotgun_snapshot.live_dmg,
            )
    

    @staticmethod
    def create_magazine(magazine_snapshot: MagazineSnapshot) -> Union[MagazineInterface, MagazineBase]:
        return MagazineBase(
            lives=magazine_snapshot.lives,
            blanks=magazine_snapshot.blanks,
            tube=magazine_snapshot.tube
        )

class ShotgunHandler:
    
    @staticmethod
    def reload_magazine(snapshot: GameSnapshot) -> GameSnapshot:
        new_snapshot = snapshot.model_copy(deep=True)
        
        magazine_snapshot = new_snapshot.shotgun.magazine
        live_magazine_obj = ShotgunFactory.create_magazine(magazine_snapshot)
        
        live_magazine_obj.reload()
        
        new_snapshot.shotgun.magazine.tube = live_magazine_obj.show(as_deque=True) # Assuming show returns deque
        
        return new_snapshot
    
    @staticmethod
    def load_chamber(snapshot: GameSnapshot) -> GameSnapshot:
        new_snapshot = snapshot.model_copy(deep=True)
        
        shotgun_snapshot = new_snapshot.shotgun
        live_shotgun_obj = ShotgunFactory.create_shotgun(shotgun_snapshot)
        
        new_snapshot.shotgun.chambered_shell = live_shotgun_obj.load_chamber()
        
        # Update the magazine state in the snapshot after loading
        new_snapshot.shotgun.magazine.tube = live_shotgun_obj.magazine.show(as_deque=True)

        return new_snapshot
    
    @staticmethod
    def unload_chamber(snapshot: GameSnapshot) -> GameSnapshot:  
        new_snapshot = snapshot.model_copy(deep=True)
        new_snapshot.shotgun.chambered_shell = None
        return new_snapshot
    
    @staticmethod
    def set_live_damage(snapshot: GameSnapshot, new_dmg:int) -> GameSnapshot:
        new_snapshot = snapshot.model_copy(deep=True)
        
        shotgun_snapshot = new_snapshot.shotgun
        live_shotgun_obj = ShotgunFactory.create_shotgun(shotgun_snapshot)
        
        live_shotgun_obj.set_live_damage(new_dmg)
        
        new_snapshot.shotgun.live_dmg = live_shotgun_obj.live_damage
        
        return new_snapshot

    @staticmethod
    def is_shell_loaded(snapshot: GameSnapshot) -> bool:
        return snapshot.shotgun.chambered_shell is not None   
    
    @staticmethod
    def get_shell(snapshot: GameSnapshot) -> Union[Shell,None]:
        return snapshot.shotgun.chambered_shell
    
    @staticmethod
    def get_live_damage(snapshot: GameSnapshot) -> int:
        return snapshot.shotgun.live_dmg