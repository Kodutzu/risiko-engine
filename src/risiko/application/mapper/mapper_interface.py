from abc import ABC, abstractmethod

class MapperInterface(ABC):

    @staticmethod
    @abstractmethod
    def assemble(snapshot: object) -> object:
        pass

    @staticmethod
    @abstractmethod
    def disassemble(interface: object) -> object:
        pass
