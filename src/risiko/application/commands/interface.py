from abc import ABC, abstractmethod
from ..game_state import GameState


class CommandInterface(ABC):

    @abstractmethod
    def work(self,state: GameState ) -> None:
        ...