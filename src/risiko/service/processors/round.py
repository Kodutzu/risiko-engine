from attrs import evolve
from ..risiko_state import RisikoState
from typing import Iterable

from ...core.shell import ShellBase, ShellData, InvalidShell


def load_round(game_state: RisikoState, round:  Iterable[ShellData] ) -> RisikoState:

    """
    Loads a new round into the shotgun magazine based on a list of shell configurations.

    Args:
        game_state (RisikoState): The current state of the game.
        round (List[LoadShell]): A list describing the shells to load, including type, damage, and quantity.

    Returns:
        RisikoState: A new game state with the updated shotgun magazine.
    """

    shells = []
    for shell in round:
        if not isinstance(shell.get("shell_type"), str) or not isinstance(shell.get("damage"), int):
        
            raise InvalidShell(f"Invalid shell data format in round: {shell}")
    
        shells.append(

            ShellBase(shell_type=shell["shell_type"], damage=shell["damage"])
        )

    new_magazine = game_state.shotgun.magazine._load_round(shells)

    return evolve(game_state, shotgun=evolve(game_state.shotgun, magazine=new_magazine))


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









