from collections import deque
from random import shuffle

from attrs import evolve

from ...core.shell import InvalidShell, ShellInterface, ShellNotFoundException
from ..risiko_state import RisikoState

def eject_magazine_shell(game_state: RisikoState):
    """
    Ejects a shell from the shotgun's magazine.

    Args:
        game_state (RisikoState): The current state of the game.

    Returns:
        Tuple[ShellInterface, RisikoState]: A tuple containing the ejected shell and the new game state.
    """

    shell_ejected, new_magazine = game_state.shotgun.magazine.eject_shell()

    return (
        shell_ejected,
        evolve(game_state, shotgun=evolve(game_state.shotgun, magazine=new_magazine)),
    )


def insert_shell_to_magazine(game_state: RisikoState, shell: ShellInterface) -> RisikoState:
    """
    Adds a shell to the shotgun's magazine.

    Args:
        game_state (RisikoState): The current state of the game.
        shell (ShellInterface): The shell to add to the magazine.

    Returns:
        RisikoState: A new game state with the shell added to the magazine.
    """

    if not isinstance(shell, ShellInterface):
        raise InvalidShell(f"Invalid object provided. Expected a ShellInterface, but got {type(shell)}.")

    new_tube = deque(game_state.shotgun.magazine.tube)
    new_tube.append(shell)

    return evolve(
        game_state,
        shotgun=evolve(
            game_state.shotgun,
            magazine=evolve(game_state.shotgun.magazine, tube=new_tube)
        )
    )


def remove_shell_from_magazine(game_state: RisikoState, shell: ShellInterface) -> RisikoState:
    """
    Removes a shell from the shotgun's magazine.

    Args:
        game_state (RisikoState): The current state of the game.
        shell (ShellInterface): The shell to remove from the magazine.

    Returns:
        RisikoState: A new game state with the shell removed from the magazine.
    """
    if not isinstance(shell, ShellInterface):
        raise InvalidShell(f"Invalid object provided. Expected a ShellInterface, but got {type(shell)}.")

    try:
        new_tube = deque(game_state.shotgun.magazine.tube)
        new_tube.remove(shell)
    except ValueError:
        raise ShellNotFoundException(f"Shell not found in magazine: {shell}")

    return evolve(
        game_state,
        shotgun=evolve(
            game_state.shotgun,
            magazine=evolve(game_state.shotgun.magazine, tube=new_tube),
        ),
    )


def shuffle_magazine(game_state: RisikoState):
    """
    Shuffles the shells in the shotgun's magazine.

    Args:
        game_state (RisikoState): The current state of the game.

    Returns:
        RisikoState: A new game state with the shells shuffled in the magazine.
    """

    new_tube = deque(game_state.shotgun.magazine.tube)
    shuffle(new_tube)

    return evolve(
        game_state,
        shotgun=evolve(
            game_state.shotgun,
            magazine=evolve(game_state.shotgun.magazine, tube=new_tube),
        ),
    )


def clear_magazine(game_state: RisikoState):
    """

    Clears all shells from the shotgun's magazine.

    Args:
        game_state (RisikoState): The current state of the game.

    Returns:
        RisikoState: A new game state with an empty magazine.

    """
    new_magazine = game_state.shotgun.magazine.clear()

    return evolve(game_state, shotgun=evolve(game_state.shotgun, magazine=new_magazine))