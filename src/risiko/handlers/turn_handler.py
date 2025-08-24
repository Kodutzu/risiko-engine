from typing import Dict

from ..core.game.snapshot import GameSnapshot
from ..core.player.snapshot import PlayerSnapshot
from ..core.player.exceptions import PlayerNotFoundException
from .handler_base import HandlerBase

class TurnHandler(HandlerBase):


    @staticmethod
    def advance_turn(snapshot: GameSnapshot) -> GameSnapshot:

        new_snapshot = snapshot.model_copy(deep=True)

        num_players = len(new_snapshot.turns.player_turn_order)
        
        new_index = (new_snapshot.turns.current_player_index+ new_snapshot.turns.direction) % num_players

        new_snapshot.turns.current_player_index = new_index

        return new_snapshot

    @staticmethod
    def reverse_order(snapshot: GameSnapshot) -> GameSnapshot:

        new_snapshot = snapshot.model_copy(deep=True)

        new_snapshot.turns.direction *= -1

        return new_snapshot
    
    
    @staticmethod
    def get_current_player(snapshot: GameSnapshot) -> Dict[int, PlayerSnapshot]:

        if not snapshot.players: 
            raise PlayerNotFoundException("No players found in the game.") 
        
        current_player_id = snapshot.turns.player_turn_order[snapshot.turns.current_player_index]
        current_player = snapshot.players.get(current_player_id)

        return {current_player_id: current_player}