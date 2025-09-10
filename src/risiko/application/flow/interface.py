#Implementing State Pattern which handles Entire State of the Game (GameState Specifically)

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..game_state import GameState

class FlowInterface(ABC):

    @abstractmethod
    def process(self, context=GameState) -> None:
        ...