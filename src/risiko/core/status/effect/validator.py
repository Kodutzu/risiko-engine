from attrs import Attribute
from typing import Any

def is_not_negative(instance: Any, attribute: Attribute, value: int) -> None:
    """Attrs validator that checks if a value is positive."""
    if value < 0:
        raise ValueError(f"'{attribute.name}' must be positive, but got {value}")