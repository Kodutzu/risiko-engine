from typing import Deque
from collections import deque
from attrs import define, field, Factory, evolve
from attrs.validators import in_


@define(frozen=True)
class TurnManager:
    
    _player_order: Deque[str] = field(default=Factory(deque),converter=deque, alias="player_order") 
    _direction: int = field(default=1, converter=int,validator=in_((-1, 1)), alias="direction")

    @property
    def current_player_id(self) -> str :

        try:
            return self._player_order[0]
        except IndexError:
            raise IndexError("There is no player in the game.")
    
    @property
    def player_order(self) -> Deque[str] :
        
        return self._player_order
    
    def remove_id(self, id:str) -> "TurnManager":

        try:
            new_player_order = self._player_order.copy()
            new_player_order.remove(id)

            return evolve(self, player_order=new_player_order)

        except ValueError:

            raise ValueError("There is no player with this ID.")

    def add_id(self, id: str) -> "TurnManager":

        if id in self._player_order:

            raise ValueError("There is already a player with this ID.")
        
        new_player_order = self._player_order.copy()
        new_player_order.append(id)

        return evolve(self, player_order=new_player_order)
    
    def advance(self) -> "TurnManager":

        new_player_order = self._player_order.copy()
        new_player_order.rotate(self._direction) #rotate left

        return evolve(self, player_order=new_player_order)

    def reverse_order(self, new_direction:int) -> "TurnManager":

        return evolve(self, direction=new_direction)
    
