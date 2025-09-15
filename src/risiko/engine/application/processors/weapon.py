from attrs import evolve
from ..risiko_state import RisikoState
from ...core.magazine.exception import MagazineException
from ..rules import has_mixed_bullets

def show_loaded_shell(game_state: RisikoState):

    """
    Returns the shell currently loaded in the shotgun's chamber.

    Args:
        game_state (RisikoState): The current state of the game.

    Returns:
        ShellInterface: The shell in the chamber, or None if the chamber is empty.

    """

    return game_state._shotgun.chamber


def show_magazines_tube(game_state: RisikoState):

    """
    Returns the current contents of the shotgun's magazine tube.

    Args:
        game_state (RisikoState): The current state of the game.

    Returns:
        Deque[ShellInterface]: A deque representing the shells in the magazine tube.
    """

    return game_state._shotgun.magazine.tube


def shotgun_load_shell(game_state:RisikoState):

    """
    Loads a shell from the magazine into the shotgun's chamber.

    Args:
        game_state (RisikoState): The current state of the game.

    Returns:
        RisikoState: A new game state with the shotgun's chamber loaded.

    Raises:
        MagazineException: If there are no mixed bullets in the magazine (based on game rules).
    """

    if not has_mixed_bullets(game_state):
        raise MagazineException("No mixed bullets in the magazine - clear and reload ")
    
    new_shotgun = game_state._shotgun.load_chamber()

    return evolve(game_state, shotgun=new_shotgun)

def unload_shotgun_chamber(game_state:RisikoState):

    """

    Unloads the shell from the shotgun's chamber back into the magazine.

    Args:
        game_state (RisikoState): The current state of the game.

    Returns:
        RisikoState: A new game state with the shotgun's chamber unloaded.

    """

    new_shotgun = game_state._shotgun.unload_chamber()

    return evolve(game_state, shotgun=new_shotgun)

def clear_magazine(game_state: RisikoState):

    """

    Clears all shells from the shotgun's magazine.

    Args:
        game_state (RisikoState): The current state of the game.

    Returns:
        RisikoState: A new game state with an empty magazine.
        
    """
    new_magazine = game_state._shotgun.magazine.clear()

    return evolve(game_state, shotgun=evolve(game_state._shotgun, magazine = new_magazine))

