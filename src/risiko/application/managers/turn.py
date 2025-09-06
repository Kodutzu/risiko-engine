from typing import Deque
from collections import deque
from attrs import define, field, Factory
from attrs.validators import ge, le


@define
class TurnManager:
    
    _player_order: Deque[str] = field(default=Factory(deque),converter=deque, alias="player_order") #accepts dict
    _direction: int = field(default=1, converter=int,validator=[ge(-1),le(1)], alias="direction")

    @property
    def current_id(self) -> str :

        try:
            return self._player_order[0]
        except IndexError:
            raise IndexError("There is no player in the game.")
    
    @property
    def all_ids(self) -> Deque[str] :
        
        return self._player_order
    
    def remove_id(self, id:str) -> None:

        try:

            self._player_order.remove(id)

        except ValueError:

            raise ValueError("There is no player with this ID.")

    def add_id(self, id: str) -> None:

        if id in self._player_order:

            raise ValueError("There is already a player with this ID.")
        
        self._player_order.append(id)
    
    def advance(self, rotation: int) -> None:

        self._player_order.rotate(self._direction*rotation) #rotate left

    def stay(self) -> None: #Does Nothing, but added just for readability!
        pass 


    def reverse_order(self, new_direction:int) -> None:

        self._direction = new_direction
    
