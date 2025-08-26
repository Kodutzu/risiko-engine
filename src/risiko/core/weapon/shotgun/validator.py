from attrs import Attribute
from typing import Any
    
def live_dmg_checker(instance: Any, attribute: Attribute, value: int):
    
    if value < 1:
        raise ValueError("Live Damage cannot be less than 1")