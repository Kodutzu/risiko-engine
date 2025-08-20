from pydantic import BaseModel, Field
from typing import List
from ...core.player.snapshot import PlayerSnapshot
from ...core.shotgun.snapshot import ShotgunSnapshot
from ...constants.game_state import GameState

class GameSnapshot(BaseModel):
    game_state: GameState
    round_number: int = 0
    current_player_index: int = 0 
    shotgun: ShotgunSnapshot = Field(default_factory=ShotgunSnapshot)
    players: List[PlayerSnapshot] = Field(default_factory=list)
    direction: int = 1
