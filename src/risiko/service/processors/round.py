from attrs import evolve
from ..risiko_state import RisikoState


def load_new_round(game_state: RisikoState, lives:int, blanks: int):

    """
    load a new round by loading the shotgun magazine with a specified number of live and blank shells.

    Args:
        game_state (RisikoState): The current state of the game.
        lives (int): The number of live shells to load.
        blanks (int): The number of blank shells to load.

    Returns:
        RisikoState: A new game state with the updated shotgun magazine.
    """

    new_magazine = game_state._shotgun.magazine.load_round(lives=lives,blanks= blanks)

    return evolve(game_state, shotgun=evolve(game_state._shotgun, magazine=new_magazine))

def advance_player_turn(game_state:RisikoState, turns: int = 1):

    """
    Advances the player turn by a specified number of turns.

    Args:
        game_state (RisikoState): The current state of the game.
        turns (int, optional): The number of turns to advance. Defaults to 1.

    Returns:
        RisikoState: A new game state with the advanced turn order.
    """

    new_turn_manager = game_state.turns._advance(turns)

    return evolve(game_state, turns=new_turn_manager)

def reverse_turn_order(game_state:RisikoState) -> RisikoState:

    """
    Reverses the direction of the player turn order.

    Args:
        game_state (RisikoState): The current state of the game.

    Returns:
        RisikoState: A new game state with the reversed turn order direction.
    """
    
    new_turn_manager = game_state.turns._reverse_order()
    return evolve(game_state, turns=new_turn_manager)









