from typing import Iterable
from attrs import define, field

from .service import RisikoState, processors
from .core.shell.dto import ShellData

@define
class RisikoEngine:
    """
    The core game engine for Risiko, providing a stateful wrapper to manage game progression
    and interactions. This class exposes a high-level API for game operations, abstracting
    the underlying state management and processing logic.

    It handles player management, shell loading and firing, and turn progression,
    ensuring game rules and state transitions are correctly applied.
    """
    _state: RisikoState = field(factory=RisikoState, init=False)

    @property
    def game_state(self) -> RisikoState:
        """
        Returns the current game state.

        Returns:
            RisikoState: The current state of the game.
        """
        return self._state

    @game_state.setter
    def game_state(self, new_state: RisikoState) -> None:
        """
        Updates the game state with a new state.

        Args:
            new_state (RisikoState): The new state of the game.
        """
        self._state = new_state

    def add_player(self, id: str, charges: int) -> None:
        """
        Adds a new player to the game.

        Args:
            id (str): The ID of the new player.
            charges (int): The initial charges (lives) for the new player.
        """
        self._state = processors.add_player_to_game(self._state, id, charges)
        

    def remove_player(self, id: str) -> None:
        """
        Removes a player from the game.

        Args:
            id (str): The ID of the player to remove.
        """
        self._state = processors.remove_player_from_game(self._state, id)


    def load_round(self, round: Iterable[ShellData]) -> None:
        """
        Loads a new round of shells into the magazine.

        Args:
            round (Iterable[ShellData]): The round of shells to load.
        """
        self._state = processors.load_magazine(self._state, round)

    def load_shell(self) -> None:
        """
        Loads a shell from the magazine into the chamber.
        """
        self._state = processors.shotgun_load_shell(self._state)


    def unload_shell(self) -> None:
        """
        Unloads a shell from the chamber back into the magazine.
        """
        self._state = processors.unload_shotgun_chamber(self._state)
    

    def fire(self, target_id: str) -> None:
        """
        Fires the shotgun at a target. The shooter is determined by the current turn.

        Args:
            target_id (str): The ID of the player being shot at.
        """
        shooter_id = self._state.turns.current_player_id
        fired_shell, self._state = processors.fire_shell(self._state, shooter_id)
        self._state = processors.hit_shell(self._state, target_id, fired_shell)
    
