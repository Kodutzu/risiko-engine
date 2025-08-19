from ..core.shotgun.shotgun import Magazine
from ..core.game.snapshot import GameSnapshot

class ShotgunHandler:
    
    @staticmethod
    def reload_magazine(snapshot: GameSnapshot, live:int = 4, blank:int = 4) -> GameSnapshot:
        
        snapshot_reload = snapshot.model_copy(deep=True)

        temp_magazine = Magazine(live, blank) #Creating a temp magazine object

        bullet_order_list = temp_magazine.reload()
        
        snapshot_reload.shotgun.magazine = bullet_order_list

        return snapshot_reload