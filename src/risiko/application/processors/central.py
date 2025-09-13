from attrs import evolve
from ..game_state import GameState
from ...core.shell.interface import ShellInterface
from ...core.shell.blank import BlankShell
from ...core.shell.live import LiveShell


def start_new_round(game_state:GameState, lives:int, blanks: int):

    new_magazine = game_state.shotgun.magazine.load_round(lives=lives,blanks= blanks)

    return evolve(game_state, shotgun=evolve(game_state.shotgun, magazine=new_magazine))

def advance_player_turn(game_state:GameState):

    new_turn_manager = game_state.turns.advance()

    return evolve(game_state, turns=new_turn_manager)

def shotgun_load_shell(game_state:GameState):
    
    new_shotgun = game_state.shotgun.load_chamber()

    return evolve(game_state, shotgun=new_shotgun)

def unload_shotgun_chamber(game_state:GameState):

    new_shotgun = game_state.shotgun.unload_chamber()

    return evolve(game_state, shotgun=new_shotgun)

def eject_magazine_shell(game_state: GameState):

    shell_ejected, new_magazine = game_state.shotgun.magazine.eject_shell()

    return (shell_ejected, evolve(game_state, shotgun=evolve(game_state.shotgun, magazine = new_magazine)))


def clear_magazine(game_state:GameState):

    new_magazine = game_state.shotgun.magazine.clear()

    return evolve(game_state, shotgun=evolve(game_state.shotgun, magazine = new_magazine))

def fire_shell(game_state:GameState):

    fired_shell,new_shotgun = game_state.shotgun.fire()
    
    return (fired_shell, evolve(game_state, shotgun=new_shotgun))

def hit_shell(game_state:GameState, target_id: str, fired_shell: ShellInterface ):

    target_player = game_state.player.get_player(target_id)

    target_player.lose_charges(fired_shell.damage)

    new_player_manager = game_state.player.update_player(target_player)

    return evolve(game_state, players=new_player_manager)







