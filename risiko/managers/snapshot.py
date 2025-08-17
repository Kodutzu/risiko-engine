from pydantic import BaseModel, Field
from typing import List, Dict, Union

class PlayerSnapshot(BaseModel):
    id: int = Field(default=0)
    charge: int = Field(default=4)
    inventory: List[str] = Field(default_factory=list)
    effects: Dict[str,int] = Field(default_factory=dict)

class ShotgunSnapshot(BaseModel):
    magazine: List[str] = Field(default_factory=list)
    shell: Union[str, None ] = Field(default=None)
    live_dmg: int  = Field(default=1)
    effects: Dict[str, int] = Field(default_factory=dict)

class GameSnapshot(BaseModel):
    game_state: str 
    current_player_id: int 
    round_number: int 
    players: List[PlayerSnapshot] = Field(default_factory=list)
    shotgun: ShotgunSnapshot = Field(default_factory=ShotgunSnapshot)