from .game_state import GameState
from ..core.shell.blank import BlankShell
from ..core.shell.live import LiveShell


def is_game_over(game_state: GameState) -> bool:
    """
    Checks if the game has reached an end condition.
    """
    alive_players = [
        p for p in game_state.player.get_all_player().values() if p.charges > 0
    ]
    return len(alive_players) <= 1

def can_player_act(game_state: GameState, player_id: str) -> bool:
    """
    Checks if a specific player is allowed to take an action.
    """
    # Is it their turn?
    if game_state.turns.current_player_id != player_id:
        return False
        
    # Are they alive?
    player = game_state.player.get_player(player_id)
    if not player.charges > 0:
        return False
        
    # Is the shotgun loaded?
    if game_state.shotgun.chamber is None:
        return False

    return True


def has_mixed_bullets(self, game_state: GameState) -> bool:

        has_live = any(isinstance(shell, LiveShell) for shell in game_state.shotgun.magazine.tube) 
        has_blank = any(isinstance(shell, BlankShell) for shell in game_state.shotgun.magazine.tube)
        
        return has_live and has_blank