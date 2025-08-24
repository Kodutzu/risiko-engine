from abc import ABC, abstractmethod

class FactoryInterface(ABC):

    @staticmethod
    @abstractmethod
    def assemble(live_snapshot, live_base) :
        pass
    