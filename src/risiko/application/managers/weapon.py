from attrs import define, field, Factory
from attrs.validators import instance_of    
from typing import Dict


from ...application.characters.shotgun.behaviour import ShotgunBehaviour
from ...application.characters.magazine.behaviour import MagazineBehaviour

@define
class WeaponManager:
    
    _shotgun_behaviour: ShotgunBehaviour = field(validator=instance_of(ShotgunBehaviour))


    def load_round(self,live:int, blank: int):
        self._shotgun_behaviour.magazine_behaviour.load_new_round(live,blank)

    def load_chamber(self):
        self._shotgun_behaviour.load_chamber()

    def eject_current_shell(self):
        self._shotgun_behaviour.magazine_behaviour.eject_current_shell()

    def fire(self):
        self._shotgun_behaviour.fire()

    def clear_magazine(self):
        self._shotgun_behaviour.magazine_behaviour.clear_shell()


        