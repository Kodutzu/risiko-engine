from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..behaviour import ShotgunBehaviour


class ShotgunState(ABC):

    @abstractmethod
    def load_chamber(self, context: "ShotgunBehaviour"): ...

    @abstractmethod
    def fire(self, context: "ShotgunBehaviour"): ...
