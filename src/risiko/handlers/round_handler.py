from ..core.game.snapshot import GameSnapshot


class RoundHandler:

    @staticmethod
    def get_current_round(snapshot: GameSnapshot) -> int:
        """Returns the current round number from the snapshot."""
        return snapshot.rounds.total

    @staticmethod
    def advance_round(snapshot: GameSnapshot) -> GameSnapshot:

        """Increments the round number and returns a new snapshot."""

        new_snapshot = snapshot.model_copy(deep=True)
        new_snapshot.rounds.total += 1
        return new_snapshot
    
    @staticmethod
    def is_round_over(snapshot: GameSnapshot) -> bool:
        """
        Checks if the round has ended by seeing if the magazine is empty.
    
        """
        return not snapshot.shotgun.magazine

    @staticmethod
    def reset_round_counter(snapshot: GameSnapshot) -> GameSnapshot:   
        """Resets the round counter to 0 and returns a new snapshot."""
        new_snapshot = snapshot.model_copy(deep=True)
        new_snapshot.rounds.total = 0
        return new_snapshot