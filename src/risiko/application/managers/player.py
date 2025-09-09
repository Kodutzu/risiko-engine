from attrs import define, field, Factory
from typing import Dict


from ...application.characters.player.behaviour import PlayerBehaviour 

@define
class PlayerManager:
    
    players: Dict[str, PlayerBehaviour] = field(default=Factory(dict), converter=dict, alias="player_list")

    def get_player(self, player_id: str) :
        try:
            return self.players[player_id]
        except KeyError:
            raise KeyError("There is no player with this ID.")
        
    def get_all_player(self) -> Dict[str, PlayerBehaviour]:
        return self.players
    
    def add_player(self, player: PlayerBehaviour) -> None:
        
        self.players.setdefault(player.id, player)

    def remove_player(self, player_id: str) -> None:
        try:
            del self.players[player_id]
        except KeyError:
            raise KeyError("There is no player with this ID.")
    

    
        