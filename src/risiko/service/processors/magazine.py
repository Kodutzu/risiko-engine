from attrs import evolve
from typing import Iterable
from random import shuffle
from collections import deque

from ..risiko_state import RisikoState
from ...core.shell import ShellData, ShellBase, InvalidShell, ShellNotFoundException


def load_magazine(game_state: RisikoState, round:  Iterable[ShellData] ) -> RisikoState:

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
        if not isinstance(shell.shell_type, str) or not isinstance(shell.damage, int):
        
            raise InvalidShell(f"Invalid shell data format in round: {shell}")
    
        shells.append(

            ShellBase(shell_type=shell.shell_type, damage=shell.damage)
        )

    new_magazine = game_state.shotgun.magazine._load_round(shells)

    return evolve(game_state, shotgun=evolve(game_state.shotgun, magazine=new_magazine))


def eject_magazine_shell(game_state: RisikoState):

    """
    Ejects a shell from the shotgun's magazine.

    Args:
        game_state (RisikoState): The current state of the game.

    Returns:
        Tuple[ShellInterface, RisikoState]: A tuple containing the ejected shell and the new game state.
    """

    shell_ejected, new_magazine = game_state.shotgun.magazine._eject_shell()

    return (shell_ejected, evolve(game_state, shotgun=evolve(game_state.shotgun, magazine = new_magazine)))


def insert_shell_to_magazine(game_state:RisikoState, shell: ShellData):

    """
    Adds a shell to the shotgun's magazine.

    Args:
        game_state (RisikoState): The current state of the game.
        shell (Literal["live", "blank"]): The shell to add to the magazine.

    Returns:
        RisikoState: A new game state with the shell added to the magazine.
    """

    if not isinstance(shell.shell_type, str) or not isinstance(shell.damage, int):
        raise InvalidShell(f"Invalid shell data format in round: {shell}")

    new_tube = deque(game_state.shotgun.magazine.tube)

    new_tube.append(ShellBase(shell_type=shell.shell_type, damage=shell.damage))

    return evolve(game_state, shotgun=evolve(game_state.shotgun, magazine = evolve(game_state.shotgun.magazine, tube = new_tube)))


def remove_shell_from_magazine(game_state:RisikoState, shell: ShellData):

    """
    Removes a shell from the shotgun's magazine.

    Args:
        game_state (RisikoState): The current state of the game.
        shell (Literal["live", "blank"]): The shell to remove from the magazine.

    Returns:
        RisikoState: A new game state with the shell removed from the magazine.
    """
    if not isinstance(shell.shell_type, str) or not isinstance(shell.damage, int):
        raise InvalidShell(f"Invalid shell data format in round: {shell}")
    
    try:
        new_tube = deque(game_state.shotgun.magazine.tube)
        new_tube.remove(ShellBase(shell_type=shell.shell_type, damage=shell.damage))

    except ValueError:
        raise ShellNotFoundException(f"Shell not found in magazine: {shell}")

    return evolve(game_state, shotgun=evolve(game_state.shotgun, magazine = evolve(game_state.shotgun.magazine, tube = new_tube)))


def shuffle_magazine(game_state:RisikoState):

    """
    Shuffles the shells in the shotgun's magazine.

    Args:
        game_state (RisikoState): The current state of the game.

    Returns:
        RisikoState: A new game state with the shells shuffled in the magazine.
    """

    new_tube = deque(game_state.shotgun.magazine.tube)
    shuffle(new_tube)
    
    return evolve(game_state, shotgun=evolve(game_state.shotgun, magazine = evolve(game_state.shotgun.magazine, tube = new_tube)))


def clear_magazine(game_state: RisikoState):

    """

    Clears all shells from the shotgun's magazine.

    Args:
        game_state (RisikoState): The current state of the game.

    Returns:
        RisikoState: A new game state with an empty magazine.
        
    """
    new_magazine = game_state.shotgun.magazine._clear()

    return evolve(game_state, shotgun=evolve(game_state.shotgun, magazine = new_magazine))

