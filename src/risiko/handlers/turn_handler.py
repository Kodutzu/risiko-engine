from ..core.game.snapshot import GameSnapshot
from ..core.player.base import Player
class TurnHandler:


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
    def get_current_player(snapshot: GameSnapshot) -> Player:

        if not snapshot.players: #Returning Null if there are no players
            raise Exception("No players") #Adding Custom Excemtion in Player's Package
        
        current_player_id = snapshot.turns.player_turn_order[snapshot.turns.current_player_index]
        current_player = snapshot.players.get(current_player_id)

        return {current_player_id: current_player}