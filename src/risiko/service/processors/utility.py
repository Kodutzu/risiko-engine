from attrs import evolve
from typing import Literal
from random import shuffle
from collections import deque

from ..risiko_state import RisikoState
from ...core.shell import ShellData,ShellBase,ShellNotFoundException, InvalidShell



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

    if not isinstance(shell.get("shell_type"), str) or not isinstance(shell.get("damage"), int):
        raise InvalidShell(f"Invalid shell data format in round: {shell}")

    new_tube = deque(game_state.shotgun.magazine.tube)

    new_tube.append(ShellBase(shell_type=shell["shell_type"], damage=shell["damage"]))

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
    if not isinstance(shell.get("shell_type"), str) or not isinstance(shell.get("damage"), int):
        raise InvalidShell(f"Invalid shell data format in round: {shell}")
    
    try:
        new_tube = deque(game_state.shotgun.magazine.tube)
        new_tube.remove(ShellBase(shell_type=shell["shell_type"], damage=shell["damage"]))
    except ValueError:
        raise ShellNotFoundException("Shell not found in magazine")

    return evolve(game_state, shotgun=evolve(game_state.shotgun, magazine = evolve(game_state.shotgun.magazine, tube = new_tube)))

def replace_chamber_shell_from_shotgun(game_state:RisikoState, shell: ShellData):

    """
    Replaces the shell in the shotgun's chamber with a new shell.

    Args:
        game_state (RisikoState): The current state of the game.
        shell (Literal["live", "blank"]): The shell to replace the current shell in the chamber.

    Returns:
        RisikoState: A new game state with the shell replaced in the chamber.
    """
    
    if not isinstance(shell.get("shell_type"), str) or not isinstance(shell.get("damage"), int):
        raise InvalidShell(f"Invalid shell data format in round: {shell}")
    
    return evolve(game_state, shotgun=evolve(game_state.shotgun, chamber = ShellBase(shell_type=shell["shell_type"], damage=shell["damage"])))

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



def player_lose_charges(game_state:RisikoState, player_id: str, charges_to_lose:int):

    """
    Makes a player lose a specified number of charges.

    Args:
        game_state (RisikoState): The current state of the game.
        player_id (str): The ID of the player who will lose charges.
        charges_to_lose (int): The number of charges to deduct.

    Returns:
        RisikoState: A new game state with the player's updated charges.
    """
    
    player = game_state.player.get_player(player_id)

    updated_player = player._lose_charges(charges_to_lose)

    new_player_manager = game_state.player._update_player(player=updated_player)

    return evolve(game_state, player=new_player_manager)

def player_gain_charges(game_state:RisikoState, player_id: str, charges_to_gain:int):

    """
    Makes a player gain a specified number of charges.

    Args:
        game_state (RisikoState): The current state of the game.
        player_id (str): The ID of the player who will gain charges.
        charges_to_gain (int): The number of charges to add.

    Returns:
        RisikoState: A new game state with the player's updated charges.
    """
    
    player = game_state.player.get_player(player_id)

    updated_player = player._gain_charges(charges_to_gain)

    new_player_manager = game_state.player._update_player(player=updated_player)

    return evolve(game_state, player=new_player_manager)


