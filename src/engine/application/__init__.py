# src/risiko/application/__init__.py

from .risiko_state import RisikoState
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
    "RisikoState",
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