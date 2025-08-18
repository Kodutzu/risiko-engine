from pydantic import BaseModel, Field
from typing import List
from .player_snapshot import PlayerSnapshot
from .shotgun_snapshot import ShotgunSnapshot

class GameSnapshot(BaseModel):
    game_state: str 
    round_number: int = 1
    current_player_index: int = 0 
    shotgun: ShotgunSnapshot = Field(default_factory=ShotgunSnapshot)
    players: List[PlayerSnapshot] = Field(default_factory=list)
    direction: int = 1
