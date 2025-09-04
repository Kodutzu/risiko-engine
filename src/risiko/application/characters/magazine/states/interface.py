from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional
from .....core.weapon.shell import Shell 

if TYPE_CHECKING:
    from ..behaviour import MagazineBehaviour


class MagazineState(ABC):

    @abstractmethod
    def load_round(self, context: "MagazineBehaviour",lives: int , blanks: int) -> Optional[None]:

        pass

    @abstractmethod
    def ejection(self, context: "MagazineBehaviour") -> Optional[Shell]:
        # Removal lof Shell from Magazine
        pass

    @abstractmethod
    def clear(self, context: "MagazineBehaviour") -> None:
        pass
