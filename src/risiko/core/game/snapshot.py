from pydantic import BaseModel, Field
from typing import Dict, List
from ...core.player.snapshot import PlayerSnapshot
from ...core.shotgun.snapshot import ShotgunSnapshot
from ...constants.game_state import GameState

class TurnSnapshot(BaseModel):
    current_player_index: int = 0 
    player_turn_order: List[str] = Field(default_factory=list)
    direction: int = 1

class RoundSnapshot(BaseModel):
    total: int
class GameSnapshot(BaseModel):
    game_state: GameState
    shotgun: ShotgunSnapshot = Field(default_factory=ShotgunSnapshot)
    players: Dict[str, PlayerSnapshot] = Field(default_factory=dict)
    turns: TurnSnapshot = Field(default_factory=TurnSnapshot)
    rounds: RoundSnapshot = Field(default_factory=RoundSnapshot)
