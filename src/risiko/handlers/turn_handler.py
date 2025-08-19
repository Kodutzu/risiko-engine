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

        snapshot_advance_turn = snapshot.model_copy(deep=True)

        current_player_index = snapshot_advance_turn.current_player_index
        
        direction = snapshot_advance_turn.direction

        num_players = len(snapshot_advance_turn.players)
        
        new_index = (current_player_index+ direction) % num_players

        snapshot_advance_turn.current_player_index = new_index

        return snapshot_advance_turn

    @staticmethod
    def reverse_order(snapshot: GameSnapshot) -> GameSnapshot:

        snapshot_reverse_order = snapshot.model_copy(deep=True)

        snapshot_reverse_order.direction *= -1

        return snapshot_reverse_order

    @staticmethod
    def update_order(snapshot: GameSnapshot, new_player_order: List[Player]) -> GameSnapshot:

        """Updates the turn order and returns a new snapshot."""

        snapshot_update_order = snapshot.model_copy(deep=True)

        snapshot_update_order.players = new_player_order

        return snapshot_update_order