from enum import Enum

class GamePhase(Enum):
    SETUP = "setup"  # Configure game (single-player level or multiplayer rules)
    INITIALIZE = "initialize"  # Set up round (shotgun, items)
    PLAYER_TURN = "player_turn"  # Player chooses action
    PROMPT_ACTION = "prompt_action"  #Prompt user for action (Shoot or Usage of Item)
    LEVEL_END = "level_end"  # End round, advance level or reset
    PAUSE = "pause"  # Halt game (menu, disconnect)
    SAVE_GAME = "save_game"  # Save state to backend
    GAME_OVER = "game_over"  # Game ends, determine winner
    RESULTS = "results"  # Show final results
    WAITING_FOR_PLAYERS = "waiting_for_players"  # Multiplayer lobby (optional)


class SystemState(Enum):
    RUNNING = "running"
    PAUSED = "paused"
    GAME_OVER = "game_over"