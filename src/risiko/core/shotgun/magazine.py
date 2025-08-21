from ...constants.shell import Shell
from pydantic import BaseModel, Field, model_validator, PrivateAttr
from typing import List, Union
from collections import deque, Counter
from .exceptions import MagazineException
import random 


class Magazine(BaseModel):
    lives: int = Field(default=4,ge=1, frozen=True)
    blanks: int = Field(default=4,ge=1, frozen=True)
    tube: deque[Shell] = Field(default_factory=deque)
    
    @model_validator(mode="after")
    def _initiate_tube(self) -> "Magazine":
        if not self.tube:
            self.tube = deque([Shell.LIVE] * self.lives + [Shell.BLANK] * self.blanks)
            self.reload()
        return self
    def reload(self) -> None:

        random.shuffle(self.tube)

    def show(self, as_list=True) -> Union[List[Shell], Counter[Shell, int]]:

        if as_list :
            return [shell for shell  in self.tube ]
        else:
            return Counter(self.tube)

    def has_mixed_bullets(self) -> bool:

        return Shell.LIVE in self.tube and Shell.BLANK in self.tube
        
    def take_out_bullet(self) -> Shell:
        
        if not self.has_mixed_bullets():
            raise MagazineException("Reload: Magazine does not have a mix of live and blank shells.")
        
        if not self.tube:
            raise MagazineException("Reload: Magazine is empty.")
        
        shell =  self.tube.popleft()

        return shell
    
    def __repr__(self) -> str:
        return f"Magazine(tube={self.tube},lives={self.lives}, blanks={self.blanks})"