from attrs import evolve
from ..risiko_state import RisikoState

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
    new_shotgun = game_state.shotgun._load_chamber()

    return evolve(game_state, shotgun=new_shotgun)

def unload_shotgun_chamber(game_state:RisikoState):

    """

    Unloads the shell from the shotgun's chamber back into the magazine.

    Args:
        game_state (RisikoState): The current state of the game.

    Returns:
        RisikoState: A new game state with the shotgun's chamber unloaded.

    """

    new_shotgun = game_state.shotgun._unload_chamber()

    return evolve(game_state, shotgun=new_shotgun)

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

