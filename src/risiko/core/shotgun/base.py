from typing import Optional, Tuple
from attrs import define, field, evolve
from attrs.validators import instance_of

from ..shell.interface import ShellInterface
from ..magazine.interface import MagazineInterface
from ..magazine.base import MagazineBase

@define(frozen=True)
class ShotgunBase:

    magazine: MagazineInterface = field(factory=MagazineBase,validator=instance_of(MagazineInterface))
    chamber: Optional[ShellInterface] = field(default=None, validator=instance_of((ShellInterface, type(None))))

    def load_chamber(self) -> "ShotgunBase":
        
      
        new_chamber, new_magazine = self.magazine.eject_shell()

        return evolve(self, chamber=new_chamber, magazine=new_magazine)

    
    def unload_chamber(self) -> "ShotgunBase":

        if isinstance(self.chamber,ShellInterface):

            self.magazine.tube.appendleft(self.chamber)

        return evolve(self, chamber=None)

    
    def fire(self) -> Tuple[ShellInterface, "ShotgunBase"]:


        if not isinstance(self.chamber,ShellInterface):

            raise Exception("Shotgun is not loaded")

        if self.chamber is None:

            raise Exception("Shotgun is not loaded")
        
        fired_shell = self.chamber

        return (fired_shell, evolve(self, chamber=None))

