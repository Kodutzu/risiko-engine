from attrs import Attribute
from typing import Any
from .exceptions import CapacityExceeded


def capacity_check(instance: Any,attribute: Attribute, value: int) -> None:

    if value <4:
        raise CapacityExceeded(f"{attribute.name} must be greater than or equal to 4")