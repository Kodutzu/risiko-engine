from attrs import define, field, evolve
from typing import Dict
from types import MappingProxyType

from ...core.player.interface import PlayerInterface
from ...core.player.exception import PlayerIDExistsException, PlayerIDNotFoundException

@define(frozen=True)
class PlayerManager:
    """
    Manages the collection of players in the game. It is an immutable class.
    All methods that modify the player collection return a new PlayerManager instance.
    """
    _pool: Dict[str, PlayerInterface] = field(factory=dict)

    def get_player(self, player_id: str) -> PlayerInterface:

        """
        Retrieves a player by their ID.

        Args:
            player_id (str): The ID of the player to retrieve.

        Returns:
            PlayerInterface: The player object.

        Raises:
            PlayerIDNotFoundException: If no player with the given ID exists.
        """
        try:
            return self._pool[player_id]
        except KeyError:
            raise PlayerIDNotFoundException(id=player_id, info="couldn't able to get the player")
        
    def get_all_player(self) -> MappingProxyType[str, PlayerInterface]:

        """
        Returns a dictionary of all players currently managed.

        Returns:

            Dict[str, PlayerInterface]: A dictionary where keys are player IDs and values are player objects.

        """
        if not self._pool:
            return MappingProxyType({}) # Return empty dict if pool is empty
        return MappingProxyType(self._pool)
    
    def _add_player(self, player: PlayerInterface) -> 'PlayerManager':

        """

        Adds a new player to the manager.

        Args:
            player (PlayerInterface): The playerBase object to add.

        Returns:
            PlayerManager: A new PlayerManager instance with the added player.

        Raises:
            PlayerIDExistsException: If a player with the same ID already exists.
        """
        if player.id in self._pool:
            raise PlayerIDExistsException(id=player.id, info=f"couldn't able to add the player")

        new_pool = self._pool.copy()
        new_pool[player.id] = player 

        return evolve(self, pool=new_pool)
    
    def _update_player(self, player: PlayerInterface) -> "PlayerManager":

        """

        Updates an existing player in the manager.

        Args:
            player (PlayerInterface): The player object with updated information.

        Returns:
            PlayerManager: A new PlayerManager instance with the updated player.

        Raises:
            PlayerIDNotFoundException: If no player with the given ID exists to update.

        """
        if player.id not in self._pool:
            raise PlayerIDNotFoundException(id=player.id, info="couldn't able to update the player")
        
        new_pool = self._pool.copy()
        new_pool[player.id] = player

        return evolve(self, pool=new_pool)

    def _remove_player(self, player_id: str) -> 'PlayerManager':
        
        """
        Removes a player from the manager by their ID.

        Args:
            player_id (str): The ID of the player to remove.

        Returns:
            PlayerManager: A new PlayerManager instance without the removed player.

        Raises:
            PlayerIDNotFoundException: If no player with the given ID exists to remove.
        """
        if player_id not in self._pool:
            raise PlayerIDNotFoundException(id=player_id, info="couldn't able to remove the player")

        new_pool = self._pool.copy()
        del new_pool[player_id]

        return evolve(self, pool=new_pool)