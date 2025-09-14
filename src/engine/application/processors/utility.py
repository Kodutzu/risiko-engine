from attrs import evolve
from ..risiko_state import RisikoState

def eject_magazine_shell(game_state: RisikoState):

    """
    Ejects a shell from the shotgun's magazine.

    Args:
        game_state (RisikoState): The current state of the game.

    Returns:
        Tuple[ShellInterface, RisikoState]: A tuple containing the ejected shell and the new game state.
    """

    shell_ejected, new_magazine = game_state._shotgun.magazine.eject_shell()

    return (shell_ejected, evolve(game_state, shotgun=evolve(game_state._shotgun, magazine = new_magazine)))

def player_lose_charge(game_state:RisikoState, player_id: str, charges_to_lose:int):

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

    updated_player = player.lose_charges(charges_to_lose)

    new_player_manager = game_state.player._update_player(player=updated_player)

    return evolve(game_state, player=new_player_manager)