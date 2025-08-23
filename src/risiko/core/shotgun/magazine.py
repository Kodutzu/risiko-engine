from ...constants.shell import Shell
from .interface import MagazineInterface
from .validator import bullet_number_checker
from attrs import define, field, setters
from typing import Deque, Union
from collections import deque, Counter
from .exceptions import MagazineException
import random 

@define
class MagazineBase(MagazineInterface):

    tube: Deque[Shell] = field(default_factory=deque)
    lives: int = field(default=4,validator=bullet_number_checker, on_setattr=setters.frozen)
    blanks: int = field(default=4, on_setattr=setters.frozen)

    def __attrs_post_init__(self):

        if not self.tube:
            self.tube = deque([Shell.LIVE] * self.lives + [Shell.BLANK] * self.blanks)
            self.reload()

    def reload(self) -> None:

        random.shuffle(self.tube)

    def show(self, as_deque=True) -> Union[Deque[Shell], Counter[Shell, int]]:

        if as_deque :
            return deque([shell for shell  in self.tube ])
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