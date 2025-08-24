from abc import ABC, abstractmethod

class MapperInterface(ABC):

    @staticmethod
    @abstractmethod
    def disassemble(interface, snapshot):
        pass
