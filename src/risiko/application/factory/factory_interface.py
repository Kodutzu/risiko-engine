from abc import ABC, abstractmethod

class FactoryInterface(ABC):

    @staticmethod
    @abstractmethod
    def create(live_snapshot, live_base) :
        pass 