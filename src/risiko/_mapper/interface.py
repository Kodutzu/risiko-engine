from abc import ABC, abstractmethod

class MapperInterface(ABC):

    @staticmethod
    @abstractmethod
    def to_snapshot(live_object):
        pass

    @staticmethod
    @abstractmethod
    def from_snapshot(snapshot):
        pass
