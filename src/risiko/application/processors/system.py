from attrs import evolve
from ..game_state import GameState
from ...core.player.base import PlayerBase

def add_player_to_game(game_state: GameState, id: str, charges: int) -> GameState:
    
    new_player_manager = game_state.player.add_player(player=PlayerBase(player_id=id, charges=charges))
    new_turn_manager = game_state.turns.add_id(id)
    
    return evolve(game_state, players=new_player_manager, turns=new_turn_manager)

def remove_player_from_game(game_state: GameState, id: str) -> GameState:

    new_player_manager = game_state.player.remove_player(player_id=id)
    new_turn_manager = game_state.turns.remove_id(id)

    return evolve(game_state, players=new_player_manager, turns=new_turn_manager)

def custom_turn_order(game_state:GameState, id:str) -> GameState:

    ...

def reverse_turn_order(game_state:GameState) -> GameState:
    ...