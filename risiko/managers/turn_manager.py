from pydantic import BaseModel, Field, PrivateAttr, model_validator
from typing import Deque, List
from ..core.player import Player
class TurnManager(BaseModel):

    players: Deque[Player] = Field(..., description="List of Player objects in game")
    direction: int = Field(default=1, ge=-1, le=1,ne=0 )

    class Config:
        arbitrary_types_allowed = True  


    @property
    def current_player(self) -> Player:

        return self.players[-1] # Returns the Last Element

    def isPlayerTurn(self, player: Player) -> bool:

        return player.id == self.current_player.id

    def advance_turn(self) -> Player:

        self.players.rotate(self.direction)
    
    def reverse_order(self, dir) -> None:

        self.direction = dir

    def remove_player(self, player: Player) -> None:
        
        self.players.remove(player)

    def add_player(self, player: Player) -> None:

        self.players.append(player)
    
    def reset_turn(self) -> None:
        self.direction = 1
    
    def total_players(self) -> int:

        return len(self.players)
    
    def get_turn_order(self) -> List[Player]:
        
            player_tuple = [player.id for player in self.players] 
            return player_tuple
