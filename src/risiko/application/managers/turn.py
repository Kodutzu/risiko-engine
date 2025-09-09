from typing import Deque, List
from collections import deque
from attrs import define, field, Factory
from attrs.validators import ge, le


@define
class TurnManager:
    
    _player_order: Deque[str] = field(default=Factory(deque),converter=deque, alias="player_order") #accepts Player ID
    _direction: int = field(default=1, converter=int,validator=[ge(-1),le(1)], alias="direction")
    _skip_list: List = field(default=Factory(list))

    @property
    def current_player_id(self) -> str :

        try:
            return self._player_order[0]
        except IndexError:
            raise IndexError("There is no player in the game.")
    
    @property
    def all_player_ids(self) -> Deque[str] :
        
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
    
    def advance(self) -> None:

        self._player_order.rotate(self._direction) #rotate left

        if self._player_order[0] in self._skip_list:
            self._skip_list.remove(self._player_order[0])
            self.advance()


    def stay(self) -> None: #Does Nothing, but added just for readability!
        pass 

    def skip(self, id: str) -> None:

        self._skip_list.append(self._player_order[0])

    def reverse_order(self, new_direction:int) -> None:

        self._direction = new_direction
    
