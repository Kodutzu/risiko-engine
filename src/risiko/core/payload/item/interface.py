from abc import ABC, abstractmethod

class ItemInterface(ABC):

    @property
    @abstractmethod
    def entity(self):
        pass
