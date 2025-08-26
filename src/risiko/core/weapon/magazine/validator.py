from attrs import Attribute
from typing import Any

def bullet_number_checker(instance: Any, attribute: Attribute, value: int):
    
    if value < 1:
        raise ValueError("Bullet number cannot be less than 1")