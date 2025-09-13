from attrs import define, field, evolve
from typing import Dict


from ...core.player.interface import PlayerInterface

@define(frozen=True)
class PlayerManager:
    
    _players: Dict[str, PlayerInterface] = field(factory=dict, alias="player_dict")


    def get_player(self, player_id: str) :
        try:
            return self._players[player_id]
        except KeyError:
            raise KeyError("There is no player with this ID.")
        
    def get_all_player(self) -> Dict[str, PlayerInterface]:

        return self._players
    
    def add_player(self, player: PlayerInterface) -> 'PlayerManager':

        if player.id in self._players:

            raise ValueError(f"Player with ID '{player.id}' already exists.")
        
 
        new_players = self._players.copy()
        new_players[player.id] = player 

        return evolve(self, players=new_players)
    
    def update_player(self, player: PlayerInterface) -> "PlayerManager":
        ...

    def remove_player(self, player_id: str) -> 'PlayerManager':
        try:
            new_players = self._players
            del new_players[player_id]

            return evolve(self, players=new_players)
        
        except KeyError:
            raise KeyError("There is no player with this ID.")
    

    
        