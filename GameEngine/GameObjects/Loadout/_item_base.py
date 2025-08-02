
from abc import ABC, abstractmethod
from dataclasses import dataclass
from ..Exception.item_exception import ItemException


@dataclass
class _ItemBase(ABC):

    def validate(self, obj:object, expected_type:object):
        if not isinstance(obj, expected_type):
            raise ItemException(
                f"{self.__class__.__name__}.use() expected {expected_type.__name__}, got {type(obj).__name__}"
            )
    @abstractmethod
    def use(self,user,target):
        pass
  
    def __str__(self):
        return self.__class__.__name__

