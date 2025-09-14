from typing import Deque
from collections import deque
from attrs import define, field, Factory, evolve
from attrs.validators import in_

from ...core.player.exception import PlayerIDExistsException, PlayerIDNotFoundException


@define(frozen=True)
class TurnManager:
    """Manages the turn order and direction of play for players in the game.
    It is an immutable class; all methods that modify the turn order or direction
    return a new TurnManager instance.
    """
    
    player_order: Deque[str] = field(default=Factory(deque), converter=deque) 
    direction: int = field(default=1, converter=int, validator=in_((-1, 1)))

    @property
    def current_player_id(self) -> str:
        
        """
        Returns the ID of the player whose turn it currently is.

        Returns:
            str: The ID of the current player.

        Raises:
            PlayerIDNotFoundException: If the player order is empty.
        """
        try:
            return self.player_order[0]
        
        except IndexError:

            raise PlayerIDNotFoundException(id="<None>", info="Player order is empty, cannot get current player.")
    
    def _remove_id(self, id:str) -> "TurnManager":
        """
        Removes a player from the turn order.

        Args:
            id (str): The ID of the player to remove.

        Returns:
            TurnManager: A new TurnManager instance with the player removed.

        Raises:
            PlayerIDNotFoundException: If the player ID is not found in the turn order.
        """
        try:
            new_player_order = self.player_order.copy()

            new_player_order.remove(id)

            return evolve(self, player_order=new_player_order)
        
        except ValueError:

            raise PlayerIDNotFoundException(id=id, info="There is no player with this ID.")

    def _add_id(self, id: str) -> "TurnManager":
        """
        Adds a player to the end of the turn order.

        Args:
            id (str): The ID of the player to add.

        Returns:
            TurnManager: A new TurnManager instance with the player added.

        Raises:
            PlayerIDExistsException: If the player ID already exists in the turn order.
        """
        if id in self.player_order:

            raise PlayerIDExistsException(id=id, info="couldn't able to add the player")
        
        new_player_order = self.player_order.copy()

        new_player_order.append(id)

        return evolve(self, player_order=new_player_order)
    
    def _advance(self, turns: int = 1) -> "TurnManager":
        """
        Advances the turn order by a specified number of turns.

        Args:
            turns (int, optional): The number of turns to advance. Defaults to 1.

        Returns:
            TurnManager: A new TurnManager instance with the advanced turn order.
        """
        new_player_order = self.player_order.copy()

        new_player_order.rotate(-(turns * self.direction))

        return evolve(self, player_order=new_player_order)

    def _reverse_order(self) -> "TurnManager":
        """
        Reverses the direction of the turn order.

        Returns:
            TurnManager: A new TurnManager instance with the reversed direction.
        """
        return evolve(self, direction=self.direction * -1)