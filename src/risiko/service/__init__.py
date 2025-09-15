# src/risiko/application/__init__.py

from .risiko_state import RisikoState

from .processors import (
    fire_shell,
    hit_shell,
    shoot,
    load_new_round,
    advance_player_turn,
    reverse_turn_order,
    add_player_to_game,
    remove_player_from_game,
    eject_magazine_shell,
    player_lose_charge,
    show_loaded_shell,
    show_magazines_tube,
    shotgun_load_shell,
    unload_shotgun_chamber,
    clear_magazine
)
from .rules import (
    is_game_over,
    is_player_alive,
    is_player_turn,
    can_player_act,
    has_mixed_bullets,
    can_load_shell,
    can_fire_shotgun,
    can_clear_magazine,
    is_magazine_empty,
    is_magazine_stocked,
    is_chamber_empty,
    is_valid_target,
    can_start_game,
)


__all__ = [

    # From processors
    "RisikoState",
    "fire_shell",
    "hit_shell",
    "shoot",
    "load_new_round",
    "advance_player_turn",
    "reverse_turn_order",
    "add_player_to_game",
    "remove_player_from_game",
    "eject_magazine_shell",
    "player_lose_charge",
    "show_loaded_shell",
    "show_magazines_tube",
    "shotgun_load_shell",
    "unload_shotgun_chamber",
    "clear_magazine",

    #rules
    "is_game_over",
    "is_player_alive",
    "is_player_turn",
    "can_player_act",
    "has_mixed_bullets",
    "can_load_shell",
    "can_fire_shotgun",
    "can_clear_magazine",
    "is_magazine_empty",
    "is_magazine_stocked",
    "is_chamber_empty",
    "is_valid_target",
    "can_start_game",

]