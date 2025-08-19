from ..core.shotgun.shotgun import Magazine
from ..core.shotgun.shotgun import Shotgun
from ..core.game.snapshot import GameSnapshot

class ShotgunHandler: # Use Config to configure the game
    
    @staticmethod
    def reload_magazine(snapshot: GameSnapshot, live:int = 4, blank:int = 4) -> GameSnapshot:
        
        snapshot_reload = snapshot.model_copy(deep=True)

        magazine = Magazine(live, blank) 

        bullet_order_list = magazine.reload()
        
        snapshot_reload.shotgun.magazine = bullet_order_list

        return snapshot_reload
    
    @staticmethod
    def load_chamber(snapshot: GameSnapshot) -> GameSnapshot:
        
        snapshot_reload = snapshot.model_copy(deep=True)
        pass


        return snapshot_reload