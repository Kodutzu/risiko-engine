from typing import List
from ..core.game.snapshot import GameSnapshot
from ..core.player.player import Player
class TurnHandler:

    @staticmethod
    def get_current_player(snapshot: GameSnapshot) -> Player | None:

        if not snapshot.players: #Returning Null if there are no players
            return None #raise an exception?
        
        current_player = snapshot.players[snapshot.current_player_index]

        return current_player

    @staticmethod
    def advance_turn(snapshot: GameSnapshot) -> GameSnapshot:

        new_snapshot = snapshot.model_copy(deep=True)
        
        num_players = len(new_snapshot.players)
        
        new_index = (new_snapshot.current_player_index+ new_snapshot.direction) % num_players
        new_snapshot.current_player_index = new_index

        return new_snapshot

    @staticmethod
    def reverse_order(snapshot: GameSnapshot) -> GameSnapshot:

        new_snapshot = snapshot.model_copy(deep=True)

        new_snapshot.direction *= -1

        return new_snapshot

    @staticmethod
    def update_order(snapshot: GameSnapshot, new_player_order: List[Player]) -> GameSnapshot:
        """Updates the turn order and returns a new snapshot."""
        new_snapshot = snapshot.model_copy(deep=True)

        new_snapshot.players = new_player_order

        return new_snapshot