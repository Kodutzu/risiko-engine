from abc import ABC, abstractmethod
from ...constants.usable_entity import UsableEntity

class EffectInterface(ABC):

    @property
    @abstractmethod
    def entity(self) -> UsableEntity:
        pass

    @property
    @abstractmethod
    def turns(self) -> int:
        pass

    @property
    @abstractmethod
    def is_active(self) -> bool:
        pass

    @abstractmethod
    def reduce_turn(self) -> None:
        pass
