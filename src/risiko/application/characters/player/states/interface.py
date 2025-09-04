from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..behaviour import PlayerBehaviour


class PlayerState(ABC):

    @abstractmethod
    def lose_charges(self, context: "PlayerBehaviour"):

        pass

    @abstractmethod
    def gain_charges(self, context: "PlayerBehaviour"):
       
        pass


