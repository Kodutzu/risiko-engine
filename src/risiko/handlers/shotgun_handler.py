from typing import Union

from ..factory.shotgun_factory import ShotgunFactory, MagazineFactory
from ..core.game.snapshot import GameSnapshot
from ..constants.shell import Shell
from .handler_base  import HandlerBase


class ShotgunHandler(HandlerBase):
    
    @staticmethod
    def reload_magazine(snapshot: GameSnapshot) -> GameSnapshot:
        new_snapshot = snapshot.model_copy(deep=True)
        
        magazine_snapshot = new_snapshot.shotgun.magazine
        live_magazine_obj = MagazineFactory.assemble(magazine_snapshot)
        
        live_magazine_obj.reload()
        
        new_snapshot.shotgun.magazine.tube = live_magazine_obj.show()
        
        return new_snapshot
    
    @staticmethod
    def load_chamber(snapshot: GameSnapshot) -> GameSnapshot:
        new_snapshot = snapshot.model_copy(deep=True)
        
        shotgun_snapshot = new_snapshot.shotgun
        live_shotgun_obj = ShotgunFactory.assemble(shotgun_snapshot)
        
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
        live_shotgun_obj = ShotgunFactory.assemble(shotgun_snapshot)
        
        live_shotgun_obj.live_damage = new_dmg
        
        new_snapshot.shotgun.live_damage = live_shotgun_obj.live_damage
        
        return new_snapshot

    @staticmethod
    def is_shell_loaded(snapshot: GameSnapshot) -> bool:
        return snapshot.shotgun.chambered_shell is not None   
    
    @staticmethod
    def get_shell(snapshot: GameSnapshot) -> Union[Shell,None]:
        return snapshot.shotgun.chambered_shell
    
    @staticmethod
    def get_live_damage(snapshot: GameSnapshot) -> int:
        return snapshot.shotgun.live_damage