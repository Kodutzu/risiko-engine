from attrs import define, field
from attrs.validators import  ge, instance_of

from ...application.characters.magazine.behaviour import MagazineBehaviour

@define
class RoundManager:
  
    _round_number: int = field(default=0, validator=ge(0), init=False, alias="round_number")
    _magazine: MagazineBehaviour = field(validator=instance_of(MagazineBehaviour), alias="magazine")

    @property
    def round_number(self) -> int:
        
        return self._round_number

    def start_round(self):
     
        self._round_number += 1
       

    def is_round_over(self):
        if not self._magazine.show(format="deque"):
            return True
        # It asks the expert for the information it needs to make a decision.
        