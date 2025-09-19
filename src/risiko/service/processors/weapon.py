from attrs import evolve
from ..risiko_state import RisikoState
from ...core.shell import ShellData,ShellBase, InvalidShell

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




def replace_chamber_shell_from_shotgun(game_state:RisikoState, shell: ShellData):

    """
    Replaces the shell in the shotgun's chamber with a new shell.

    Args:
        game_state (RisikoState): The current state of the game.
        shell (Literal["live", "blank"]): The shell to replace the current shell in the chamber.

    Returns:
        RisikoState: A new game state with the shell replaced in the chamber.
    """
    
    if not isinstance(shell.shell_type, str) or not isinstance(shell.damage, int):
        raise InvalidShell(f"Invalid shell data format in round: {shell}")
    
    return evolve(game_state, shotgun=evolve(game_state.shotgun, chamber = ShellBase(shell_type=shell.shell_type, damage=shell.damage)))

