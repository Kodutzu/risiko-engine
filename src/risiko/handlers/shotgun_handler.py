from ..core.shotgun.shotgun import Shotgun, Magazine,Shell
from ..core.game.snapshot import GameSnapshot
from typing import Union

class ShotgunHandler:
    
    @staticmethod
    def reload_magazine(snapshot: GameSnapshot) -> GameSnapshot:
        
        new_snapshot = snapshot.model_copy(deep=True)

        magazine = Magazine(lives = new_snapshot.shotgun.magazine.lives, blanks = new_snapshot.shotgun.magazine.blanks) 

        shell_order_list = magazine.reload()
        
        new_snapshot.shotgun.magazine = shell_order_list

        return new_snapshot
    
    @staticmethod
    def load_chamber(snapshot: GameSnapshot) -> GameSnapshot:
        
        new_snapshot = snapshot.model_copy(deep=True)

        shotgun = Shotgun(magazine=Magazine(tube=new_snapshot.shotgun.magazine.tube))

        new_snapshot.shotgun.chambered_shell = shotgun.load_chamber()

        return new_snapshot
    
    @staticmethod
    def unload_chamber(snapshot: GameSnapshot) -> GameSnapshot:  
        
        new_snapshot = snapshot.model_copy(deep=True)

        new_snapshot.shotgun.chambered_shell = None

        return new_snapshot
    
    @staticmethod
    def set_live_damage(snapshot: GameSnapshot, new_dmg:int) -> GameSnapshot:
        
        new_snapshot = snapshot.model_copy(deep=True)

        shotgun = Shotgun() #default values has been initialized

        shotgun.set_live_damage(new_dmg)

        new_snapshot.shotgun.live_dmg = shotgun.live_damage

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
    

