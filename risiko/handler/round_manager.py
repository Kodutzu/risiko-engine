from pydantic import BaseModel, Field, PrivateAttr
from ..core.player import Player   
from typing import List

class RoundHandler:
    pass

# class RoundManager(BaseModel):
#     players: List[Player] = Field(..., description="List of Player objects in game")
#     _current_round: int = PrivateAttr(default=0)


#     @property
#     def current_round(self): 
#         return self._current_round
    
#     def start_round(self): 
#         self._current_round += 1

#     def end_round(self): 
#         pass

#     def reset_round(self): 
#         self._current_round = 0

#     def remove_player(self, player: Player) -> None:
#         for p in self.players:
#             if p.id == player.id:
#                 self.players.remove(p)
#                 return
#         raise ValueError("Player doesn't exist")

#     def add_player(self, player: Player) -> None:
#         for p in self.players:
#             if p.id == player.id:
#                 raise ValueError("Player already in game")

#         self.players.append(player)
    
#     def total_players(self) -> int:

#         return len(self.players)




