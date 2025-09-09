#Creating Item Strategy Interface - which will have apply method!
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional, Union, overload

from ...game_state import GameState


class ItemInstructInterface(ABC):

    @abstractmethod
    def apply(self, context: GameState) -> None:
        ...


