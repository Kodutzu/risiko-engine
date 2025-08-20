from ..core.shotgun.shotgun import Shotgun, Magazine,Shell
from ..core.game.snapshot import GameSnapshot

class ShotgunHandler: # Use Config to configure the game
    
    @staticmethod
    def reload_magazine(snapshot: GameSnapshot, lives:int = 4, blanks:int = 4) -> GameSnapshot:
        
        snapshot_reload = snapshot.model_copy(deep=True)

        magazine = Magazine(lives=lives, blanks=blanks) 

        bullet_order_list = magazine.reload()
        
        snapshot_reload.shotgun.magazine = bullet_order_list

        return snapshot_reload
    
    @staticmethod
    def load_chamber(snapshot: GameSnapshot) -> GameSnapshot:
        
        snapshot_load_chamber = snapshot.model_copy(deep=True)

        tube_snapshot = snapshot_load_chamber.shotgun.magazine.tube

        shotgun = Shotgun(magazine=Magazine(tube=tube_snapshot))

        chambered_shell = shotgun.load_chamber()

        snapshot_load_chamber.shotgun.shell = chambered_shell

        return snapshot_load_chamber
    
    @staticmethod
    def unload_shell(snapshot: GameSnapshot) -> GameSnapshot:  
        
        snapshot_unload_shell = snapshot.model_copy(deep=True)

        shotgun = Shotgun(magazine=Magazine()) #default values has been initialized

        shotgun.shell.load(snapshot_unload_shell.shotgun.current_shell)

        snapshot_unload_shell.shotgun.current_shell = None

        snapshot_unload_shell.shotgun.previous_shell = shotgun.shell.unload()


        return snapshot_unload_shell

    @staticmethod
    def is_shell_loaded(snapshot: GameSnapshot) -> bool:

        return snapshot.shotgun.current_shell is not None   
    
    @staticmethod
    def get_live_damage(snapshot: GameSnapshot) -> int:

        return snapshot.shotgun.live_dmg
    
    @staticmethod
    def set_live_damage(snapshot: GameSnapshot, new_dmg:int) -> GameSnapshot:
        
        snapshot_set_live_damage = snapshot.model_copy(deep=True)

        shotgun = Shotgun(magazine=Magazine()) #default values has been initialized

        shotgun.set_live_damage(new_dmg)

        return snapshot_set_live_damage
