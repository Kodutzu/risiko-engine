from pydantic import BaseModel, Field
from typing import Dict, List
from .player_snapshot import PlayerSnapshot
from .shotgun_snapshot import ShotgunSnapshot


class TurnSnapshot(BaseModel):
    current_player_index: int = 0 
    player_turn_order: List[str] = Field(default_factory=list)
    direction: int = 1

class RoundSnapshot(BaseModel):
    total: int = 0

class GameSnapshot(BaseModel):
    # game_state: GameState 
    shotgun: ShotgunSnapshot = Field(default_factory=ShotgunSnapshot)
    players: Dict[str, PlayerSnapshot] = Field(default_factory=dict)
    turns: TurnSnapshot = Field(default_factory=TurnSnapshot)
    rounds: RoundSnapshot = Field(default_factory=RoundSnapshot)
