from attrs import define, field
from random import shuffle

from ...core.weapon.magazine.base import MagazineBase
from ...core.weapon.magazine.interface import MagazineInterface
from ...core.weapon.shell import Shell


@define
class MagazineCharacter:

    data: MagazineInterface = field(factory=MagazineBase, alias="magazine")

    def load_new_round(self, lives: int, blanks: int):

        self.data.tube.clear()
        self.data.tube.extend( ([Shell.LIVE] * lives) + ([Shell.BLANK] * blanks) )
        shuffle(self.data.tube)
        

    @property
    def has_mixed_bullets(self) -> bool:

        return (Shell.LIVE in self.data.tube) and (Shell.BLANK in self.data.tube)

    def take_out_bullet(self) -> Shell:
        
                
        if self.is_tube_empty:
            raise Exception("Reload: Magazine is empty.")
        
        if not self.has_mixed_bullets:
            raise Exception("Reload: Magazine does not have a mix of live and blank shells.")

        return self.tube.popleft()